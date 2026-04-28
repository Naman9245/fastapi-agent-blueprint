from datetime import datetime

from pydantic import BaseModel, Field

from src._core.application.dtos.base_response import BaseResponse


class ChatRequest(BaseModel):
    prompt: str = Field(..., description="User prompt", max_length=2000)


class ChatReply(BaseModel):
    reply: str = Field(..., description="Agent reply")
    confidence: float = Field(..., description="Agent confidence score")


class ChatMessageResponse(BaseResponse):
    id: int
    prompt: str
    reply: str
    confidence: float
    tokens_used: int
    created_at: datetime
