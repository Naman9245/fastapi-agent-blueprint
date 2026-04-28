from src.simple_chatbot.interface.server.schemas.chat_schema import ChatReply


class StubChatAgent:
    async def chat(self, prompt: str) -> ChatReply:
        return ChatReply(reply=f"Stub reply to: {prompt}", confidence=1.0)
