# app-telegram.py

import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import filters

from pathlib import Path

from utils.logger import Logger
logger = Logger(name='app-telegram')

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение настроек из переменных окружения
API_ID = int(os.getenv('TELEGRAM_API_ID'))
API_HASH = os.getenv('TELEGRAM_API_HASH')
USER_NAME = os.getenv('TELEGRAM_USERNAME')
CHANNEL_NAME = os.getenv('TELEGRAM_CHANNEL_NAME')

# Создание клиента Pyrogram
client = Client(name=USER_NAME, api_id=API_ID, api_hash=API_HASH)

def all_messages_handler(client: Client, message: Message):
    from_channel = message.chat.title
    from_channel_id = message.chat.id
    media_type = message.media
    photo = message.photo

    if photo:
        # Создаем директорию для сохранения изображений
        images_dir = Path(__file__).parent / 'media'
        images_dir.mkdir(exist_ok=True)
        file_name = f"{photo.file_unique_id}.jpg"
        file_path = images_dir / file_name

        client.download_media(message.photo, file_name=file_path)
        # Скачиваем фото и сохраняем в указанную директорию
        # file_path = message.download(file_name=f"{images_dir} / {file_name}")
        

        logger.info(f"Message from {from_channel} contains image: saved to {file_path}")
    else:
        logger.warning(f"Message from {from_channel} ({from_channel_id}) does not contain an image")

client.add_handler(MessageHandler(all_messages_handler, filters=filters.chat(CHANNEL_NAME)))
logger.info(f"Listening for messages in {CHANNEL_NAME}...")
client.run()

