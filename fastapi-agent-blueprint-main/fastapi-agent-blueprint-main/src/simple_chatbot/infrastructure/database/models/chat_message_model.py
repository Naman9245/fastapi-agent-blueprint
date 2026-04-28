from sqlalchemy import DateTime, Float, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src._core.infrastructure.persistence.rdb.database import Base


class ChatMessageModel(Base):
    __tablename__ = "chat_message"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    reply: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    tokens_used: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now(), nullable=True
    )
