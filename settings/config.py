# settings/config.py
import os

class Config:
    TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
    TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
    TELEGRAM_CHANNEL_NAME = os.getenv("TELEGRAM_CHANNEL_NAME")

    X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
    X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
    X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
    X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
    
    DEBUG_STATE_CONSOLE = True
    DEBUG_STATE_FILE = True