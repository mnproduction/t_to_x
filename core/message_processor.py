# core/message_processor.py
from core.interfaces import AbstractMessageProcessor

class MessageProcessor(AbstractMessageProcessor):
    def extract_image(self, message):
        if message.photo:
            file_path = message.download()
            return file_path
        return None

    def prepare_caption(self, message):
        return message.caption or ""

    def generate_content(self):
        plus_message = "+"
        return plus_message
