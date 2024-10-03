# core/manager.py
from datetime import datetime, timedelta

from core.message_processor import MessageProcessor
from apps.t.client import TelegramClient
from settings.config import Config

from utils.logger import Logger

logger = Logger(name='manager')

class AppManager:
    def __init__(self, message_receiver, content_publisher, message_processor, config: Config):
        self.message_receiver = message_receiver
        self.content_publisher = content_publisher
        self.message_processor = message_processor
        self.config = config
        self.last_sent_time = None
        self.cooldown_period = timedelta(seconds=self.config.COOLDOWN_PERIOD)

    def run(self):
        self.message_receiver.connect()
        self.content_publisher.authenticate()

        try:
            for message in self.message_receiver.get_messages():
                self.process_message(message)
        finally:
            self.message_receiver.disconnect()

    def process_message(self, message):
        current_time = datetime.utcnow()
        if self.last_sent_time and (current_time - self.last_sent_time) < self.cooldown_period:
            logger.info("Cooldown active. Skipping sending.")
            return

        content = self.message_processor.process(message)
        if content:
            self.content_publisher.publish_content(content)
            self.last_sent_time = current_time
            