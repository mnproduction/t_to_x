# apps/t/client.py
from apps.interface import AbstractMessageReceiver
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import idle
from settings.config import Config
from pathlib import Path
from utils.logger import Logger

logger = Logger(name='t-client')

class TelegramClient(AbstractMessageReceiver):
    def __init__(self, config: Config):
        self.client = Client(
            name=config.TELEGRAM_USERNAME, 
            api_id=config.TELEGRAM_API_ID, 
            api_hash=config.TELEGRAM_API_HASH,
            phone_number=config.TELEGRAM_PHONE
            )
        self.channel_name = config.TELEGRAM_CHANNEL_NAME
        self.channel_id = config.TELEGRAM_CHANNEL_ID
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)
        self.client.add_handler(handler)

    async def run(self):
        await self.client.start()
        logger.info(f"Listening for messages in {self.channel_name}...")
        await idle()
        await self.client.stop()

        



