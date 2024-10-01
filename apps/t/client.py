# apps/t/client.py
import asyncio
import socket

from pyrogram import Client, idle
from pyrogram.errors import RPCError

from apps.interface import AbstractMessageReceiver
from settings.config import Config
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
        retry_delay = 1  # Начальная задержка в секундах
        max_retry_delay = 60  # Максимальная задержка

        while True:
            try:
                logger.info("Trying to connect to Telegram...")
                await self.client.start()
                logger.info(f"Connected to {self.channel_name}. Listening for messages...")
                
                # Сбросить задержку после успешного подключения
                retry_delay = 1
                
                # Ожидание до отключения
                await idle()
                
            except (OSError, asyncio.TimeoutError, socket.gaierror) as e:
                logger.error(f"Network error occurred: {e}. Reconnecting in {retry_delay} seconds...")
                await self.client.stop()
                await asyncio.sleep(retry_delay)
                retry_delay = min(retry_delay * 2, max_retry_delay)  # Удваиваем задержку до максимума
                continue  # Повторяем цикл для переподключения
                
            except RPCError as e:
                logger.error(f"RPC error occurred: {e}. Reconnecting in {retry_delay} seconds...")
                await self.client.stop()
                await asyncio.sleep(retry_delay)
                retry_delay = min(retry_delay * 2, max_retry_delay)
                continue  # Повторяем цикл для переподключения
                
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}. Exiting...")
                await self.client.stop()
                break

