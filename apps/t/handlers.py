# apps/t/handlers.py

from io import BytesIO
import re
from typing import List
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

        try:
            if message.media_group_id is not None:
                # Handling media group
                messages: List[Message] = await client.get_media_group(chat_id=message.chat.id, message_id=message.id)
                if message.id != messages[0].id:
                    # If there's no caption, skip processing
                    return
                
                logger.info(f"Received media group with {len(messages)} items from {from_channel}")
                # Collecting files
                file_streams: List[BytesIO] = []
                for msg in messages:
                    if msg.photo:
                        # Downloading image to memory
                        file_stream = await client.download_media(msg, in_memory=True)
                        file_stream.seek(0)
                        file_streams.append(file_stream)
                    else:
                        logger.warning(f"Message in media group {message.media_group_id} does not contain a photo.")

                # Getting caption from last message
                caption = ""
                for msg in reversed(messages):
                    if msg.caption:
                        caption = msg.caption
                        break
                logger.info(f"Caption: {caption}")

                # Cleaning caption (removing all links)
                http_regexp = re.compile(r'http[s]?://[^\s]+')
                if http_regexp.search(caption):
                    logger.warning(f"Message contains links: {http_regexp.search(caption)}") 
                caption = re.sub(http_regexp, '', caption)
                logger.info(f"Cleaned caption: {caption}")

                # Publishing images to X
                media_ids = x_client.media_upload_from_files(file_streams)
                x_client.publish_content(content=caption, media_ids=media_ids)
                logger.info("Images have been posted to X")
                # Closing files
                for fs in file_streams:
                    fs.close()
            
            elif message.photo:
                # Download image to memory
                file_stream: BytesIO = await client.download_media(message, in_memory=True)
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
                file_stream.close()
            else:
                logger.warning(f"Message from {from_channel} ({from_channel_id}) does not contain an image or media group.")
        except Exception as e:
            logger.error(f"Error processing image from {from_channel}: {e}")


    handler = MessageHandler(
            photo_message_handler, 
            filters=filters.chat(telegram_client.channel_name) & filters.photo | filters.media_group
        )
    return handler
