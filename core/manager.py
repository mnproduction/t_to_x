# core/manager.py
from apps.t.client import TelegramClient
from core.message_processor import MessageProcessor

from datetime import datetime, timedelta
from utils.logger import Logger

logger = Logger(name='manager')

class AppManager:
    COOLDOWN_PERIOD = timedelta(seconds=60)  # Set cooldown period as needed

    def __init__(self, message_receiver, content_publisher, message_processor):
        self.message_receiver = message_receiver
        self.content_publisher = content_publisher
        self.message_processor = message_processor
        self.last_sent_time = None

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
        if self.last_sent_time and (current_time - self.last_sent_time) < self.COOLDOWN_PERIOD:
            logger.info("Cooldown active. Skipping sending '+'.")
            return

        content = self.message_processor.process(message)
        if content:
            self.content_publisher.publish_content(content)
            self.last_sent_time = current_time
