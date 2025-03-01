from fastapi import WebSocket, HTTPException
from sqlalchemy.orm import Session
from ..models import Message
from datetime import datetime
from ..logger import logger  

class ChatService:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket, db: Session):
        try:
            await websocket.accept()
            self.active_connections.append(websocket)
            logger.info(f"WebSocket connection established: {websocket.client}")
        except Exception as e:
            logger.error(f"Error establishing WebSocket connection: {e}")
            raise HTTPException(status_code=500, detail="Failed to establish WebSocket connection")

    async def disconnect(self, websocket: WebSocket, db: Session):
        self.active_connections.remove(websocket)
        logger.info(f"WebSocket connection closed: {websocket.client}")

    async def process_message(self, websocket: WebSocket, data: dict, db: Session):
        try:
            message = Message(
                chat_id=data["chat_id"],
                sender_id=data["sender_id"],
                text=data["text"],
                timestamp=datetime.now(),
                read=False
            )
            db.add(message)
            db.commit()
            db.refresh(message)

            for connection in self.active_connections:
                await connection.send_json(data)
            logger.info(f"Message processed: {message.id}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            raise HTTPException(status_code=500, detail="Failed to process message")

chat_service = ChatService()