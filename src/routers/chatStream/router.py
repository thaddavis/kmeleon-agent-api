from fastapi import APIRouter, Request
from langchain_openai import ChatOpenAI
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.core.schemas.Prompt import Prompt
import json
import os
from fastapi.responses import StreamingResponse
from langchain_core.prompts import ChatPromptTemplate

limiter = Limiter(key_func=get_remote_address)

from dotenv import load_dotenv

load_dotenv()

callbacks = []

router = APIRouter()

async def generator(prompt: str):
    model: str = "gpt-4o-mini"
    llm = ChatOpenAI(model=model, api_key=os.getenv("OPENAI_API_KEY"))
    promptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", "You're an assistant. Bold key terms in your responses."),
            ("human", "{input}"),
        ]
    )
    messages = promptTemplate.format_messages(input=prompt)
    async for evt in llm.astream_events(messages, version="v1", config={"callbacks": callbacks}, model=model):
        if evt["event"] == "on_chat_model_start":
            yield json.dumps({
                "event": "on_chat_model_start"
            }, separators=(',', ':'))

        elif evt["event"] == "on_chat_model_stream":
            yield json.dumps({
                "event": "on_chat_model_stream",
                "data": evt["data"]['chunk'].content
            }, separators=(',', ':'))

        elif evt["event"] == "on_chat_model_end":
            yield json.dumps({
                "event": "on_chat_model_end"
            }, separators=(',', ':'))

@router.post("/chat")
@limiter.limit("10/minute")
def prompt(prompt: Prompt, request: Request):
    return StreamingResponse(generator(prompt.prompt), media_type='text/event-stream')