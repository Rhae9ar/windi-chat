from fastapi import FastAPI
from .routers import chat, history

app = FastAPI(title="WinDI Chat API")

app.include_router(chat.router)
app.include_router(history.router)