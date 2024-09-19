from abc import ABC, abstractmethod

class IContent(ABC):

    @abstractmethod
    def create_content(self):
        pass
