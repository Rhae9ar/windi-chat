from fastapi import APIRouter, WebSocket, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import chat_service
from ..logger import logger 

from .. import models, database, services, security

router = APIRouter()

@router.websocket("/chat")
async def chat_endpoint(websocket: WebSocket, token: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    try:
        await chat_service.connect(websocket, db)
        try:
            while True:
                data = await websocket.receive_json()
                await chat_service.process_message(websocket, data, db)
        except Exception as e:
            logger.error(f"WebSocket error: {e}")
            await chat_service.disconnect(websocket, db)
    except HTTPException as e:
        logger.error(f"HTTPException in chat_endpoint: {e}")
        await websocket.close(code=1011)
    except Exception as e:
        logger.error(f"Unexpected error in chat_endpoint: {e}")
        await websocket.close(code=1011)