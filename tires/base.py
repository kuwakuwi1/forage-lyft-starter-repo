from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self):
        return self

    @abstractmethod
    def needs_service(self) -> bool:
        pass