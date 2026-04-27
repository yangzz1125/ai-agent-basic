from datetime import datetime

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=1)


class ChatResponse(BaseModel):
    answer: str


class ChatRecord(BaseModel):
    question: str
    answer: str
    created_at: datetime = Field(default_factory=datetime.now)
