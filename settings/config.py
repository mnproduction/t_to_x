# settings/config.py
import os

class Config:
    def __init__(self):
        self.TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
        self.TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
        self.TELEGRAM_PHONE = os.getenv("TELEGRAM_PHONE")
        self.TELEGRAM_USERNAME = os.getenv("TELEGRAM_USERNAME")
        self.TELEGRAM_GROUP_NAME = os.getenv("TELEGRAM_GROUP_NAME")
        self.TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")
        
        self.DEBUG_STATE_CONSOLE = True
        self.DEBUG_STATE_FILE = True

        # Проверка обязательных переменных
        required_vars = [
            "TELEGRAM_API_ID",
            "TELEGRAM_API_HASH",
            "TELEGRAM_GROUP_ID",
        ]
        for var in required_vars:
            if getattr(self, var) is None:
                raise ValueError(f"Environment variable {var} is not set.")

