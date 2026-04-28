from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src._core.application.dtos.base_response import SuccessResponse
from src.simple_chatbot.domain.services.chat_service import ChatService
from src.simple_chatbot.infrastructure.di.simple_chatbot_container import (
    SimpleChatbotContainer,
)
from src.simple_chatbot.interface.server.schemas.chat_schema import (
    ChatMessageResponse,
    ChatRequest,
)

router = APIRouter()


@router.post(
    "/chat",
    summary="Send a chat message",
    response_model=SuccessResponse[ChatMessageResponse],
    response_model_exclude={"pagination"},
)
@inject
async def create_chat(
    item: ChatRequest,
    chat_service: ChatService = Depends(Provide[SimpleChatbotContainer.chat_service]),
) -> SuccessResponse[ChatMessageResponse]:
    data = await chat_service.chat(request=item)
    return SuccessResponse(data=ChatMessageResponse(**data.model_dump()))


@router.get(
    "/chat/{message_id}",
    summary="Get chat message by ID",
    response_model=SuccessResponse[ChatMessageResponse],
    response_model_exclude={"pagination"},
)
@inject
async def get_chat_by_id(
    message_id: int,
    chat_service: ChatService = Depends(Provide[SimpleChatbotContainer.chat_service]),
) -> SuccessResponse[ChatMessageResponse]:
    data = await chat_service.get_message_by_id(message_id=message_id)
    return SuccessResponse(data=ChatMessageResponse(**data.model_dump()))
