# app.py

from apps.t.client import TelegramClient
from apps.t.handlers import create_message_handler
from settings.config import Config
from pathlib import Path

def main():
    config = Config()
    telegram_client = TelegramClient(config)

    # Директория для сохранения изображений
    images_dir = Path(__file__).parent / 'media'
    
    # Создаем обработчик сообщений
    message_handler = create_message_handler(telegram_client, images_dir)

    # Добавляем обработчик в клиента
    telegram_client.add_handler(message_handler)

    # Запускаем клиента
    telegram_client.run()

if __name__ == "__main__":
    main()
