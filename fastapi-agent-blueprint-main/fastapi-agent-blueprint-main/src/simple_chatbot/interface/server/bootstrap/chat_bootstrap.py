from fastapi import FastAPI

from src._core.infrastructure.persistence.rdb.database import Database
from src.simple_chatbot.infrastructure.di.simple_chatbot_container import (
    SimpleChatbotContainer,
)
from src.simple_chatbot.interface.server.routers import chat_router


def bootstrap_simple_chatbot_domain(
    app: FastAPI, simple_chatbot_container: SimpleChatbotContainer
) -> None:
    simple_chatbot_container.wire(
        packages=["src.simple_chatbot.interface.server.routers"]
    )
    app.include_router(router=chat_router.router, prefix="/v1", tags=["Chat"])
