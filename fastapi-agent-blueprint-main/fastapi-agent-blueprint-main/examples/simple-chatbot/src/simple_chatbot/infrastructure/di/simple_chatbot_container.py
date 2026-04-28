from dependency_injector import containers, providers

from src._core.config import settings
from src.simple_chatbot.domain.services.chat_service import ChatService
from src.simple_chatbot.infrastructure.agent.pydantic_ai_chat_agent import (
    PydanticAIChatAgent,
)
from src.simple_chatbot.infrastructure.agent.stub_chat_agent import StubChatAgent
from src.simple_chatbot.infrastructure.repositories.chat_repository import (
    ChatRepository,
)


def _agent_selector() -> str:
    return "real" if settings.llm_model_name else "stub"


class SimpleChatbotContainer(containers.DeclarativeContainer):
    core_container = providers.DependenciesContainer()
    chat_repository = providers.Singleton(
        ChatRepository, database=core_container.database
    )
    chat_agent = providers.Selector(
        _agent_selector,
        real=providers.Singleton(
            PydanticAIChatAgent, llm_model=core_container.llm_model
        ),
        stub=providers.Singleton(StubChatAgent),
    )
    chat_service = providers.Factory(
        ChatService, chat_agent=chat_agent, chat_repository=chat_repository
    )
