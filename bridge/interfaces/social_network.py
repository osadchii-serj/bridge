from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class ISocialNetwork(ABC):

    communication_api: Any
    name_network = None

    @abstractmethod
    def publish(self):
        pass
