# apps/t/handlers.py

from typing import List
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from apps.t.client import TelegramClient
from utils.logger import Logger

logger = Logger(name='telegram-handler')

class MediaGroupHandler(MessageHandler):
    def __init__(self, telegram_client: TelegramClient):
        self.telegram_client = telegram_client

    async def handle_media_group(self, client: Client, message: Message) -> None:
        from_group_id = message.chat.id

        messages: List[Message] = await client.get_media_group(chat_id=message.chat.id, message_id=message.id)
        if message.id != messages[0].id:
            # If not the first message, skip processing
            return
        logger.info(f"Received media group (ID: {message.media_group_id}) with {len(messages)} items from group: {message.chat.title} ({from_group_id})")
        try:
            await client.send_message(chat_id=from_group_id, text="+")
            logger.info(f"Sent '+' to group with ID: {from_group_id}")
        except Exception as e:
            logger.error(f"Error sending '+' to group with ID {from_group_id}: {e}")



def create_media_group_handler(telegram_client: TelegramClient) -> MessageHandler:
    handler = MediaGroupHandler(telegram_client)
    return MessageHandler(
        handler.handle_media_group, 
        filters=filters.chat(int(telegram_client.group_id)) & filters.media_group
    )

