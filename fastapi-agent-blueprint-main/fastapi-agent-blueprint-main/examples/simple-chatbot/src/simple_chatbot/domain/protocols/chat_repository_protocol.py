from src._core.domain.protocols.repository_protocol import BaseRepositoryProtocol
from src.simple_chatbot.domain.dtos.chat_message_dto import ChatMessageDTO


class ChatRepositoryProtocol(BaseRepositoryProtocol[ChatMessageDTO]):
    pass
