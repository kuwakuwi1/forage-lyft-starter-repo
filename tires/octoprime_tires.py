from abc import ABC
from tires.base import Tires

class OctoprimeTires(Tires, ABC):
    # init with parameter: array of wear_sensors with type of float between 0 and 1
    def __init__(self, wear_sensors: list[float]):
        self.wear_sensors = wear_sensors

    # return true if sum of the wear_sensors is more than or equal 3
    def needs_service(self) -> bool:
        return sum(self.wear_sensors) >= 3