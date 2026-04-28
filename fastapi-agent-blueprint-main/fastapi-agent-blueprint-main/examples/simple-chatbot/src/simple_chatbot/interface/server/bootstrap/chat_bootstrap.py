from fastapi import FastAPI
from src.simple_chatbot.infrastructure.di.chat_container import ChatContainer

from src._core.infrastructure.persistence.rdb.database import Database
from src.simple_chatbot.interface.server.routers import chat_router


def bootstrap_chat_domain(
    app: FastAPI, database: Database, chat_container: ChatContainer
) -> None:
    chat_container.wire(packages=["src.simple_chatbot.interface.server.routers"])
    app.include_router(router=chat_router.router, prefix="/v1", tags=["Chat"])
