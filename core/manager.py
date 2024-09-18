# core/manager.py
from apps.t.client import TelegramClient
from apps.x.client import XClient
from core.message_processor import MessageProcessor

class AppManager:
    def __init__(self, message_receiver, content_publisher, message_processor):
        self.message_receiver = message_receiver
        self.content_publisher = content_publisher
        self.message_processor = message_processor

    def run(self):
        self.message_receiver.connect()
        self.content_publisher.authenticate()

        try:
            for message in self.message_receiver.get_messages():
                self.process_message(message)
        finally:
            self.message_receiver.disconnect()

    def process_message(self, message):
        content = self.message_processor.process(message)
        if content:
            self.content_publisher.publish_content(content)
