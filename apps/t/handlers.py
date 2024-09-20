# apps/t/handlers.py

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pathlib import Path
from apps.t.client import TelegramClient
from utils.logger import Logger

logger = Logger(name='telegram-handler')

def create_message_handler(telegram_client, images_dir: Path):
    async def photo_message_handler(client: Client, message: Message):
        from_channel = message.chat.title
        from_channel_id = message.chat.id

        if message.photo:
            # Скачиваем фото и сохраняем в указанную директорию
            logger.info(f"Processing image from {from_channel}")
            await telegram_client.download_image(message, images_dir)
            # Здесь можно добавить код для дальнейшей обработки изображения
        else:
            logger.warning(f"Message from {from_channel} ({from_channel_id}) does not contain an image")

    handler = MessageHandler(photo_message_handler, filters=filters.chat(telegram_client.channel_name) & filters.photo)
    return handler
