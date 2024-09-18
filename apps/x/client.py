# apps/x/client.py
from apps.interface import AbstractContentPublisher
import tweepy

class XClient(AbstractContentPublisher):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        self.api = tweepy.API(self.auth)

    def authenticate(self):
        # Аутентификация происходит в конструкторе
        pass

    def publish_content(self, content):
        self.api.update_with_media(filename=content['image_path'], status=content.get('caption', ''))
