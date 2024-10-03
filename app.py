# app.py
import asyncio
import sys
import time

from apps.t.client import TelegramClient
from apps.t.handlers import create_media_group_handler
from settings.config import Config
from core.manager import AppManager
from core.message_processor import MessageProcessor
from utils.logger import Logger

logger = Logger(name='app')

async def main():
    config = Config()
    telegram_client = TelegramClient(config)

    # Initialize processors and publishers as needed
    message_processor = MessageProcessor()
    content_publisher = telegram_client  # Assuming TelegramClient handles publishing

    app_manager = AppManager(
        message_receiver=telegram_client,
        content_publisher=content_publisher,
        message_processor=message_processor,
        config=config
    )

    # Create and add handler
    media_group_handler = create_media_group_handler(telegram_client)
    telegram_client.add_handler(media_group_handler)

    max_retries = 5
    retry_delay = 5  # Start with 5 seconds

    for attempt in range(1, max_retries + 1):
        try:
            logger.info("Starting Telegram client.")
            await telegram_client.run()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            if attempt < max_retries:
                logger.info(f"Retrying in {retry_delay} seconds... (Attempt {attempt}/{max_retries})")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                logger.critical("Max retries reached. Exiting application.")
                sys.exit(1)
        else:
            break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application shutdown requested by user.")
        