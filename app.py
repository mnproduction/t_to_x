# app.py

import asyncio
from apps.t.client import TelegramClient
from apps.t.handlers import create_media_group_handler
from settings.config import Config


async def main():
    config = Config()
    telegram_client = TelegramClient(config)

    
    # Create message handler, passing x_client
    media_group_handler = create_media_group_handler(telegram_client)

    # Add handler to client
    telegram_client.add_handler(media_group_handler)

    # Run client
    await telegram_client.run()

if __name__ == "__main__":
    asyncio.run(main())

