# app.py

from apps.t.client import TelegramClient
from apps.x.client import XClient
from apps.t.handlers import create_photo_message_handler
from settings.config import Config
import asyncio


async def main():
    config = Config()
    telegram_client = TelegramClient(config)
    x_client = XClient(config)

    # Create message handler, passing x_client
    message_handler = create_photo_message_handler(telegram_client, x_client)

    # Add handler to client
    telegram_client.add_handler(message_handler)

    # Run client
    await telegram_client.run()

if __name__ == "__main__":
    asyncio.run(main())

