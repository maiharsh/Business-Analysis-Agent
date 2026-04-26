from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import analysis, chat, health

app = FastAPI(title="Agentic Business Surveillance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend access
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(health.router, prefix="/api")
