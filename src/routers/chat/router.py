from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.schemas.Prompt import Prompt
from langgraph.prebuilt import create_react_agent
import os
from langchain_core.tracers import LangChainTracer
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.postgres import PostgresSaver
from langsmith import Client
from psycopg_pool import ConnectionPool
from src.core.tools.get_weather import get_weather

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
def prompt(prompt: Prompt, request: Request):
    DB_URI=os.getenv("DB_URI")
    connection_kwargs = {
      "autocommit": True,
      "prepare_threshold": 0,
    }

    with ConnectionPool(
      conninfo=DB_URI,
      max_size=20,
      kwargs=connection_kwargs,
    ) as pool:
      checkpointer = PostgresSaver(pool)
      checkpointer.setup()
      
      # search = TavilySearchResults(max_results=2)
      tools = [get_weather]
      
      model: str = "gpt-4o-mini"
      graph = create_react_agent(model, prompt=f"You are a helpful assistant. Today's date is {datetime.now().strftime("%Y-%m-%d")}.", tools=tools, checkpointer=checkpointer)
      config = {"configurable": {"thread_id": f"{ prompt.thread_id}"}}
      res = graph.invoke({"messages": [("human", f"{prompt.content}")]}, config)
      
      last_message = res["messages"][-1].content
      return {"completion": last_message}