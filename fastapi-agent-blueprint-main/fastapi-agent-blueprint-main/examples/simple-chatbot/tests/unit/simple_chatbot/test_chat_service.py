from datetime import datetime

import pytest
from pydantic import BaseModel

from src.simple_chatbot.domain.dtos.chat_message_dto import ChatMessageDTO
from src.simple_chatbot.domain.services.chat_service import ChatService
from src.simple_chatbot.interface.server.schemas.chat_schema import (
    ChatReply,
    ChatRequest,
)


class MockChatAgent:
    async def chat(self, prompt: str) -> ChatReply:
        return ChatReply(reply=f"Mock reply to: {prompt}", confidence=0.9)


class MockChatRepository:
    def __init__(self):
        self._store: dict[int, ChatMessageDTO] = {}
        self._next_id = 1

    async def insert_data(self, entity: BaseModel) -> ChatMessageDTO:
        dto = ChatMessageDTO(
            id=self._next_id, created_at=datetime.now(), **entity.model_dump()
        )
        self._store[self._next_id] = dto
        self._next_id += 1
        return dto

    async def select_data_by_id(self, data_id: int) -> ChatMessageDTO:
        return self._store[data_id]


@pytest.fixture
def chat_service():
    return ChatService(chat_agent=MockChatAgent(), chat_repository=MockChatRepository())


@pytest.mark.asyncio
async def test_chat_creates_message(chat_service):
    result = await chat_service.chat(request=ChatRequest(prompt="Hello!"))
    assert result.id == 1
    assert result.prompt == "Hello!"
    assert result.confidence == 0.9


@pytest.mark.asyncio
async def test_get_message_by_id(chat_service):
    created = await chat_service.chat(request=ChatRequest(prompt="What is Python?"))
    fetched = await chat_service.get_message_by_id(message_id=created.id)
    assert fetched.prompt == "What is Python?"


@pytest.mark.asyncio
async def test_multiple_messages(chat_service):
    await chat_service.chat(request=ChatRequest(prompt="First"))
    await chat_service.chat(request=ChatRequest(prompt="Second"))
    assert (await chat_service.get_message_by_id(1)).prompt == "First"
    assert (await chat_service.get_message_by_id(2)).prompt == "Second"
