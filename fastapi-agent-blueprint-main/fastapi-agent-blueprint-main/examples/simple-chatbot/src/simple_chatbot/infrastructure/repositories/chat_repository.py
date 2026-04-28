from src._core.infrastructure.persistence.rdb.base_repository import BaseRepository
from src._core.infrastructure.persistence.rdb.database import Database
from src.simple_chatbot.domain.dtos.chat_message_dto import ChatMessageDTO
from src.simple_chatbot.infrastructure.database.models.chat_message_model import (
    ChatMessageModel,
)


class ChatRepository(BaseRepository[ChatMessageDTO]):
    def __init__(self, database: Database) -> None:
        super().__init__(
            database=database, model=ChatMessageModel, return_entity=ChatMessageDTO
        )
