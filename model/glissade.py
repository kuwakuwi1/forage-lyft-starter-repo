from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.splider_battery import SpliderBattery

class Glissade(Car):
    def __init__(self, engine: WilloughbyEngine, battery: SpliderBattery):
        self.engine = engine
        self.battery = battery