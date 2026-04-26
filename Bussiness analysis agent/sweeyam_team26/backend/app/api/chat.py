from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ask_agent

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    message: str
    analysis_state: dict


@router.post("/chat")
def chat_with_agent(req: ChatRequest):
    response = ask_agent(
        req.message,
        req.analysis_state
    )
    return {"response": response}
