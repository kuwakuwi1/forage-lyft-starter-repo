from abc import ABC
from tires.base import Tires

class CarriganTires(Tires, ABC):
    # init with parameter: array of wear_sensors with type of float between 0 and 1
    def __init__(self, wear_sensors: list[float]):
        self.wear_sensors = wear_sensors

    # return true if any of the wear_sensors is more than or equal 0.9
    def needs_service(self) -> bool:
        return any(wear_sensor >= 0.9 for wear_sensor in self.wear_sensors)