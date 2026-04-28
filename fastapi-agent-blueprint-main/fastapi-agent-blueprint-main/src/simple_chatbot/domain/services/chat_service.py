from pydantic import BaseModel

from src.simple_chatbot.domain.dtos.chat_message_dto import ChatMessageDTO
from src.simple_chatbot.domain.protocols.chat_repository_protocol import (
    ChatRepositoryProtocol,
)
from src.simple_chatbot.interface.server.schemas.chat_schema import ChatRequest


class _ChatInsert(BaseModel):
    prompt: str
    reply: str
    confidence: float
    tokens_used: int


class ChatService:
    def __init__(self, chat_agent, chat_repository: ChatRepositoryProtocol) -> None:
        self._agent = chat_agent
        self._repository = chat_repository

    async def chat(self, request: ChatRequest) -> ChatMessageDTO:
        reply = await self._agent.chat(prompt=request.prompt)
        return await self._repository.insert_data(
            entity=_ChatInsert(
                prompt=request.prompt,
                reply=reply.reply,
                confidence=reply.confidence,
                tokens_used=0,
            )
        )

    async def get_message_by_id(self, message_id: int) -> ChatMessageDTO:
        return await self._repository.select_data_by_id(data_id=message_id)
