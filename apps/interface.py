from abc import ABC, abstractmethod

class AbstractMessageReceiver(ABC):

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def add_handler(self, handler):
        pass

class AbstractContentPublisher(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def publish_content(self, content):
        pass