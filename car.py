from abc import ABC

from serviceable import Serviceable
from engine.base import Engine
from battery.base import Battery

class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
