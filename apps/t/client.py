# apps/t/client.py
from apps.interface import AbstractMessageReceiver
from pyrogram import Client
from pyrogram import idle
from settings.config import Config
from utils.logger import Logger

logger = Logger(name='t-client')

class TelegramClient(AbstractMessageReceiver):
    def __init__(self, config: Config):
        self.client: Client = Client(
            name=config.TELEGRAM_USERNAME, 
            api_id=config.TELEGRAM_API_ID, 
            api_hash=config.TELEGRAM_API_HASH,
            phone_number=config.TELEGRAM_PHONE,
        )
        self.group_id = config.TELEGRAM_GROUP_ID  # Use group ID from environment variables

    def add_handler(self, handler):
        self.client.add_handler(handler)

    async def run(self):
        try:
            await self.client.start()
            if not self.group_id:
                raise ValueError("TELEGRAM_GROUP_ID is not set in environment variables.")
            logger.info(f"Target group ID: {self.group_id}")
            logger.info(f"Listening for messages in group with ID {self.group_id}...")
            # Keep the client in active state
            await idle()
        except Exception as e:
            logger.error(f"Telegram client encountered an error: {e}")
            raise e  # Re-raise the exception to be caught in main
        finally:
            await self.client.stop()