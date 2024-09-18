# apps/t/client.py
from apps.interface import AbstractMessageReceiver
from pyrogram import Client

class TelegramClient(AbstractMessageReceiver):
    def __init__(self, api_id, api_hash, channel_name):
        self.client = Client("my_account", api_id, api_hash)
        self.channel_name = channel_name

    def connect(self):
        self.client.start()

    def disconnect(self):
        self.client.stop()

    def get_messages(self):
        for message in self.client.iter_history(self.channel_name):
            yield message

