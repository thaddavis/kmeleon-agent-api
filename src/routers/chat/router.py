from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.schemas.Prompt import Prompt
from langgraph.prebuilt import create_react_agent
import os
from langchain_core.tracers import LangChainTracer
from langgraph.checkpoint.postgres import PostgresSaver
from langsmith import Client
from psycopg_pool import ConnectionPool
from src.core.tools import (
   get_current_and_forecasted_weather,
   get_historical_weather_data_for_timestamp
)
from src.config.db_config import connection_kwargs
from src.middleware.get_current_user import jwt_dependency

limiter = Limiter(key_func=get_remote_address)

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

callbacks = [
  LangChainTracer(
    project_name=os.getenv("LANGSMITH_PROJECT"),
    client=Client(
      api_url=os.getenv("LANGCHAIN_ENDPOINT"),
      api_key=os.getenv("LANGCHAIN_API_KEY")
    )
  )
]

router = APIRouter()

@router.post("/chat")
@limiter.limit("10/minute")
def prompt(prompt: Prompt, jwt: jwt_dependency, request: Request):
    with ConnectionPool(
      conninfo=os.getenv("POSTGRES_URL"),
      max_size=20,
      kwargs=connection_kwargs,
    ) as pool:
      checkpointer = PostgresSaver(pool)
      checkpointer.setup()
      
      tools = [get_current_and_forecasted_weather,get_historical_weather_data_for_timestamp]
      
      model: str = "gpt-4o-mini"
      graph = create_react_agent(model, prompt=f"You are a helpful assistant. Today's date is {datetime.now().strftime("%Y-%m-%d")}.", tools=tools, checkpointer=checkpointer)
      config = {"configurable": {"thread_id": f"{ prompt.thread_id}"}}
      res = graph.invoke({"messages": [("human", f"{prompt.content}")]}, config)
      
      last_message = res["messages"][-1].content
      return {"completion": last_message}