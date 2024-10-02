import os

class Config:
    def __init__(self):
        self.TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
        self.TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
        self.TELEGRAM_PHONE = os.getenv("TELEGRAM_PHONE")
        self.TELEGRAM_USERNAME = os.getenv("TELEGRAM_USERNAME")
        self.TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

        self.X_API_KEY = os.getenv("X_API_KEY")
        self.X_API_SECRET = os.getenv("X_API_SECRET")
        self.X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
        self.X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
        self.X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
        self.X_CLIENT_ID = os.getenv("X_CLIENT_ID")
        self.X_CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
        
        self.DEBUG_STATE_CONSOLE = True
        self.DEBUG_STATE_FILE = True

        self.validate()

    def validate(self):
        required_vars = [
            "TELEGRAM_API_ID",
            "TELEGRAM_API_HASH",
            "TELEGRAM_CHANNEL_ID",
            "X_API_KEY",
            "X_API_SECRET",
            "X_ACCESS_TOKEN",
            "X_ACCESS_TOKEN_SECRET",
        ]
        for var in required_vars:
            if getattr(self, var) is None:
                raise ValueError(f"Mandatory variable not set: {var}")
