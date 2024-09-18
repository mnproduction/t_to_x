from abc import ABC, abstractmethod

class AbstractMessageReceiver(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_messages(self):
        pass

class AbstractContentPublisher(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def publish_content(self, content):
        pass