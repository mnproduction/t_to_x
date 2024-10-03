# apps/t/handlers.py
from typing import List
from pyrogram import Client, filters
from pyrogram.types import Message
from apps.t.client import TelegramClient
from core.manager import AppManager
from utils.logger import Logger

logger = Logger(name='telegram-handler')

class MediaGroupHandler:
    def __init__(self, app_manager: AppManager):
        self.app_manager = app_manager

    async def handle_media_group(self, client: Client, message: Message) -> None:
        from_group_id = message.chat.id

        messages: List[Message] = await client.get_media_group(chat_id=message.chat.id, message_id=message.id)
        if message.id != messages[0].id:
            # If not the first message, skip processing
            return
        logger.info(f"Received media group (ID: {message.media_group_id}) with {len(messages)} items from group: {message.chat.title} ({from_group_id})")
        try:
            self.app_manager.process_message(message)
            logger.info(f"Processed message and sent '+' to group with ID: {from_group_id}")
        except Exception as e:
            logger.error(f"Error processing message for group with ID {from_group_id}: {e}")



def create_media_group_handler(app_manager: AppManager):
    handler = MediaGroupHandler(app_manager)
    return handlers.MessageHandler(handler.handle_media_group, filters.media_group)

