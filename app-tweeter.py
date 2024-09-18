# app-tweeter.py
from pathlib import Path
import tweepy
from settings.config import Config

from utils.logger import Logger
logger = Logger(name='app-tweeter')


# # Получение ключей и токенов из переменных окружения
# CONSUMER_KEY = Config.X_API_KEY
# CONSUMER_SECRET = Config.X_API_SECRET
# BEARER_TOKEN = Config.X_BEARER_TOKEN
# ACCESS_TOKEN = Config.X_ACCESS_TOKEN
# ACCESS_TOKEN_SECRET = Config.X_ACCESS_TOKEN_SECRET

# # V1 API
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# # V2 API
# client = tweepy.Client(
#     bearer_token=BEARER_TOKEN,
#     consumer_key=CONSUMER_KEY,
#     consumer_secret=CONSUMER_SECRET,
#     access_token=ACCESS_TOKEN,
#     access_token_secret=ACCESS_TOKEN_SECRET
# )

# # Path

# file = Path(__file__).parent / 'media' / '5427292444308922456_120.jpg'

# # Upload image
# media_id = api.media_upload(filename=file).media_id_string
# logger.info(media_id)

# # Caption
# caption = 'Testing API'

# # Publish
# client.create_tweet(media_ids=[media_id], text=caption)
# logger.info(f"Published: {caption}")

from apps.x.client import XClient

config = Config()
xclient = XClient(config)

file_path = Path(__file__).parent / 'media' / '5427292444308922456_120.jpg'  
media_id = xclient.media_upload(file_path)
    
xclient.publish_content(media_id)