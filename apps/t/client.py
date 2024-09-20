# apps/t/client.py
from apps.interface import AbstractMessageReceiver
from pyrogram import Client
from pyrogram.types import Message
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

    def run(self):
        logger.info(f"Listening for messages in {self.channel_name}...")
        self.client.run()

    async def download_image(self, message: Message, save_dir: Path) -> Path:
        """
        Downloads image from message and saves it to specified directory.

        Args:
            message (Message): Pyrogram Message object containing image.
            save_dir (Path): Path to directory where image should be saved.

        Returns:
            Path: Path to saved image.
        """
        try:
            save_dir.mkdir(exist_ok=True)
            photo = message.photo
            file_name = f"{photo.file_unique_id}.jpg"
            file_path = save_dir / file_name

            await self.client.download_media(message, file_name=str(file_path))
            logger.info(f"Image saved to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error downloading image: {e}")
            raise e
        



