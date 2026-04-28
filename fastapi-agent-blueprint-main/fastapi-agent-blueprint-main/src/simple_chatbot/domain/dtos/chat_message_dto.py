from datetime import datetime

from pydantic import BaseModel, Field


class ChatMessageDTO(BaseModel):
    id: int = Field(..., description="Chat message unique identifier")
    prompt: str = Field(..., description="User prompt")
    reply: str = Field(..., description="Agent reply")
    confidence: float = Field(..., description="Agent confidence score")
    tokens_used: int = Field(..., description="Tokens used")
    created_at: datetime = Field(..., description="Created at")
