from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.simple_chatbot.domain.dtos.chat_message_dto import ChatMessageDTO
from src.simple_chatbot.domain.services.chat_service import ChatService
from src.simple_chatbot.interface.server.schemas.chat_schema import (
    ChatReply,
    ChatRequest,
)


class TestChatService:
    """ChatService delegates to agent and repository — uses mocks only."""

    @pytest.mark.asyncio
    async def test_chat_persists_and_returns_dto(self):
        expected_dto = ChatMessageDTO(
            id=1,
            prompt="Hello!",
            reply="Hi there!",
            confidence=0.9,
            tokens_used=0,
            created_at=datetime.now(),
        )
        mock_agent = MagicMock()
        mock_agent.chat = AsyncMock(
            return_value=ChatReply(reply="Hi there!", confidence=0.9)
        )
        mock_repo = MagicMock()
        mock_repo.insert_data = AsyncMock(return_value=expected_dto)

        service = ChatService(chat_agent=mock_agent, chat_repository=mock_repo)
        result = await service.chat(request=ChatRequest(prompt="Hello!"))

        assert result is expected_dto
        mock_agent.chat.assert_awaited_once_with(prompt="Hello!")
        mock_repo.insert_data.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_get_message_by_id(self):
        expected_dto = ChatMessageDTO(
            id=1,
            prompt="Hello!",
            reply="Hi there!",
            confidence=0.9,
            tokens_used=0,
            created_at=datetime.now(),
        )
        mock_agent = MagicMock()
        mock_repo = MagicMock()
        mock_repo.select_data_by_id = AsyncMock(return_value=expected_dto)

        service = ChatService(chat_agent=mock_agent, chat_repository=mock_repo)
        result = await service.get_message_by_id(message_id=1)

        assert result is expected_dto
        mock_repo.select_data_by_id.assert_awaited_once_with(data_id=1)

    @pytest.mark.asyncio
    async def test_chat_propagates_agent_exception(self):
        mock_agent = MagicMock()
        mock_agent.chat = AsyncMock(side_effect=RuntimeError("API timeout"))
        mock_repo = MagicMock()

        service = ChatService(chat_agent=mock_agent, chat_repository=mock_repo)
        with pytest.raises(RuntimeError, match="API timeout"):
            await service.chat(request=ChatRequest(prompt="Hello!"))
