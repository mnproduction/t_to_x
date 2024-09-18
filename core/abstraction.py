# abstract_message_processor
from abc import ABC, abstractmethod

class AbstractMessageProcessor(ABC):
    @abstractmethod
    def extract_image(self, message):
        """Extracts image from message."""
        pass

    @abstractmethod
    def prepare_caption(self, message):
        """Prepares caption for image (if necessary)."""
        pass

# abstract_manager
class AbstractManager(ABC):
    @abstractmethod
    def run(self):
        """Starts main application loop."""
        pass

    @abstractmethod
    def process_message(self, message):
        """Processes message from Telegram."""
        pass
