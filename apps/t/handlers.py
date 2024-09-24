# apps/t/handlers.py

import re
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from apps.t.client import TelegramClient
from apps.x.client import XClient
from utils.logger import Logger

logger = Logger(name='telegram-handler')

def create_photo_message_handler(telegram_client: TelegramClient, x_client: XClient):
    async def photo_message_handler(client: Client, message: Message):
        from_channel = message.chat.title
        from_channel_id = message.chat.id

        if message.photo:
            try:
                # Download image to memory
                file_stream = await client.download_media(message, in_memory=True)
                file_stream.seek(0)
                logger.info(f"Received image from {from_channel}")
                
                # Recive image caption
                caption = message.caption or ""
                logger.info(f"Caption: {caption}")
                
                # Prepare caption (delete all links from caption)
                http_regexp = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                if http_regexp.search(caption):
                    logger.warning(f"Messege contains links: {http_regexp.search(caption)}") 
                caption = re.sub(http_regexp, '', caption)
                logger.info(f"Cleaned caption: {caption}")

                # Post image to Twitter
                media_id = x_client.media_upload_from_file(file_stream)
                x_client.publish_content(content=caption, media_id=media_id)
                logger.info("Image has been posted to Twitter")
            except Exception as e:
                logger.error(f"Error processing image from {from_channel}: {e}")
            finally:
                file_stream.close()
        else:
            logger.warning(f"Message from {from_channel} ({from_channel_id}) does not contain an image")

    handler = MessageHandler(photo_message_handler, filters=filters.chat(telegram_client.channel_name) & filters.photo)
    return handler
