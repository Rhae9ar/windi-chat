from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Message
from ..logger import logger

from .. import models, database, security

router = APIRouter()

@router.get("/history/{chat_id}")
def get_history(chat_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    try:
        messages = db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.timestamp).all()
        logger.info(f"Retrieved history for chat {chat_id}")
        return messages
    except Exception as e:
        logger.error(f"Error retrieving history for chat {chat_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve chat history")