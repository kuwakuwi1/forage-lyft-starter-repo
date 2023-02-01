from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self):
        return self

    @abstractmethod
    def needs_service(self):
        pass
