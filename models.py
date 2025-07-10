from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    agent: str
    prompt: str
    model: Optional[str] = "gpt-3.5-turbo"

class ChatResponse(BaseModel):
    agent: str
    response: str
    model: str
    tokens_used: Optional[int] = None
