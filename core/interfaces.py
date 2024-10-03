from abc import ABC, abstractmethod

class AbstractMessageReceiver(ABC):
    @abstractmethod
    def add_handler(self, handler):
        pass

class AbstractContentPublisher(ABC):
    @abstractmethod
    def publish_content(self, content):
        pass

class AbstractMessageProcessor(ABC):
    @abstractmethod
    def generate_content(self, message):
        pass

# abstract_manager
class AbstractManager(ABC):
    @abstractmethod
    def run(self):
        """Starts main application loop."""
        pass

    @abstractmethod
    def stop(self):
        """Stops main application loop."""
        pass

    @abstractmethod
    def restart(self):
        """Restarts application loop."""
        pass

    @abstractmethod
    def process_message(self, message):
        """Processes message from message receiver."""
        pass

    @abstractmethod
    def publish_content(self, content):
        """Publishes content to content publisher."""
        pass

    @abstractmethod
    def cooldown(self):
        """Sets cooldown period."""
        pass

