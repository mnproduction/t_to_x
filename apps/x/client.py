# apps/x/client.py
from io import BytesIO
from typing import List
from apps.interface import AbstractContentPublisher
from tweepy import Client, API, OAuthHandler
from settings.config import Config
from pathlib import Path
from utils.logger import Logger

logger = Logger(name='x-client')

class XClient(AbstractContentPublisher):
    def __init__(self, config: Config):
        # auth v2
        self.client = Client(
            bearer_token=config.X_BEARER_TOKEN,
            consumer_key=config.X_API_KEY,
            consumer_secret=config.X_API_SECRET,
            access_token=config.X_ACCESS_TOKEN,
            access_token_secret=config.X_ACCESS_TOKEN_SECRET,
        )
        
        # auth v1.1
        self.api = API(OAuthHandler(
            consumer_key=config.X_API_KEY,
            consumer_secret=config.X_API_SECRET,
            access_token=config.X_ACCESS_TOKEN,
            access_token_secret=config.X_ACCESS_TOKEN_SECRET
        ))
    
    def authenticate(self):
        return super().authenticate()
    
    def media_upload(self, file_path: Path):
        self.media_id = self.api.media_upload(
            filename=file_path
            ).media_id_string
        logger.debug(f"Uploaded media: {self.media_id}")
        
        return self.media_id
    
    def media_upload_from_file(self, file_stream: BytesIO):
        try:
            file_stream.seek(0)
            media = self.api.media_upload(filename='image.jpg', file=file_stream)
            self.media_id = media.media_id_string
            logger.debug(f"Uploaded media: {self.media_id}")
            return self.media_id
        except Exception as e:
            logger.error(f"Error uploading media to Twitter: {e}")
            raise e

    def media_upload_from_files(self, file_streams: List[BytesIO]):
        try:
            media_ids = []
            for file_stream in file_streams:
                file_stream.seek(0)
                media = self.api.media_upload(filename='image.jpg', file=file_stream)
                media_id = media.media_id_string
                media_ids.append(media_id)
                logger.debug(f"Uploaded media: {media_id}")
            return media_ids
        except Exception as e:
            logger.error(f"Error uploading media to X: {e}")
            raise e
        
    def publish_content(self, content, media_ids=None):
        """Publishes tweet with specified content and media."""
        try:
            tweets = []
            for i in range(0, len(media_ids), 4):
                tweets.append(media_ids[i:i+4])
                
            for i, tweet in enumerate(tweets, start=1):
                self.client.create_tweet(media_ids=tweet, text=content)
                logger.info(f"Published tweet {i} with {len(tweet)} media: {content}")
        except Exception as e:
            logger.error(f"Error publishing tweet: {e}")
            raise e

