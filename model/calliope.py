from car import Car
from battery.splider_battery import SpliderBattery
from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, engine: CapuletEngine, battery: SpliderBattery):
        self.engine = engine
        self.battery = battery
