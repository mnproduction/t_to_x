import pytest
from unittest.mock import MagicMock
from core.manager import AppManager
from settings.config import Config
from datetime import datetime, timedelta

@pytest.fixture
def config():
    config = Config()
    config.COOLDOWN_PERIOD = 2  # 2 seconds for testing
    return config

@pytest.mark.asyncio
async def test_cooldown_behavior(config):
    message_receiver = MagicMock()
    content_publisher = MagicMock()
    message_processor = MagicMock()
    message_processor.process.return_value = "Test Content"

    app_manager = AppManager(
        message_receiver=message_receiver,
        content_publisher=content_publisher,
        message_processor=message_processor,
        config=config
    )

    # Simulate two messages sent within the cooldown period
    app_manager.last_sent_time = datetime.utcnow()
    app_manager.process_message("message1")
    app_manager.process_message("message2")

    # content_publisher.publish_content should only be called once
    assert content_publisher.publish_content.call_count == 1