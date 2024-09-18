# core/message_processor.py
from core.abstraction import AbstractMessageProcessor

class MessageProcessor(AbstractMessageProcessor):
    def extract_image(self, message):
        if message.photo:
            # Сохранение изображения в локальный файл
            file_path = message.download()
            return file_path
        return None

    def prepare_caption(self, message):
        return message.caption or ""
