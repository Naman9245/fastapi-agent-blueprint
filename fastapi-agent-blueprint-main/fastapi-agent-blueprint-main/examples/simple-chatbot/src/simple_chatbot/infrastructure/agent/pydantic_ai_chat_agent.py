from __future__ import annotations

from typing import Any

from src.simple_chatbot.interface.server.schemas.chat_schema import ChatReply


class PydanticAIChatAgent:
    def __init__(self, llm_model: Any) -> None:
        try:
            from pydantic_ai import Agent
        except ImportError:
            raise ImportError("pydantic-ai is required.")
        self._agent = Agent(
            model=llm_model,
            output_type=ChatReply,
            system_prompt="You are a helpful assistant. Provide a confidence score between 0.0 and 1.0.",
        )

    async def chat(self, prompt: str) -> ChatReply:
        result = await self._agent.run(prompt)
        return result.output
