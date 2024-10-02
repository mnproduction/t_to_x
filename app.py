# app.py
import asyncio
import argparse

from apps.t.client import TelegramClient
from apps.x.client import XClient
from apps.t.handlers import create_photo_message_handler
from settings.config import Config

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Run the Telegram bot")
    parser.add_argument(
        "--debug", action="store_true", help="Activate debug mode", default=False
    )
    return parser.parse_args()

async def main():
    config = Config()
    telegram_client = TelegramClient(config)
    x_client = XClient(config)

    # Create message handler, passing x_client
    message_handler = create_photo_message_handler(telegram_client, x_client)

    # Parse command-line arguments
    args: argparse.Namespace = parse_arguments()
    
    if args.debug:
        from apps.t.handlers import create_debug_message_handler
        debug_handler = create_debug_message_handler()
        telegram_client.add_handler(debug_handler)
    
    # Add handler to client
    telegram_client.add_handler(message_handler)

    # Run client
    await telegram_client.run()

if __name__ == "__main__":
    asyncio.run(main())

