from agents.chat_agent import chat_agent


def ask_agent(user_message: str, state: dict) -> str:
    return chat_agent(user_message, state)
