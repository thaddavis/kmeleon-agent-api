from pydantic import BaseModel

class Prompt(BaseModel):
    content: str
    thread_id: str