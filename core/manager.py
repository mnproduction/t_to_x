# core/manager.py
from datetime import datetime, timedelta, timezone

from core.interfaces import AbstractMessageReceiver, AbstractContentPublisher, AbstractManager
from core.message_processor import MessageProcessor
from settings.config import Config

from utils.logger import Logger

logger = Logger(name='manager')

class AppManager(AbstractManager):
    def __init__(self, message_receiver: AbstractMessageReceiver, content_publisher: AbstractContentPublisher, message_processor: MessageProcessor, config: Config):
        self.message_receiver: AbstractMessageReceiver = message_receiver
        self.content_publisher: AbstractContentPublisher = content_publisher
        self.message_processor: MessageProcessor = message_processor
        self.config = config
        self.last_sent_time = None
        self.cooldown_period = timedelta(seconds=self.config.COOLDOWN_PERIOD)

    def run(self):
        self.message_receiver.add_handler(self.process_message)


    def process_message(self, message):
        current_time = datetime.now(timezone.utc)
        if self.last_sent_time and (current_time - self.last_sent_time) < self.cooldown_period:
            logger.info("Cooldown active. Skipping sending.")
            return

        content = self.message_processor.process(message)
        if content:
            self.content_publisher.publish_content(content)
            self.last_sent_time = current_time
