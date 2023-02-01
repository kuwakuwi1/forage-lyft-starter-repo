from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(Car):
    def __init__(self, engine: WilloughbyEngine, battery: NubbinBattery):
        self.engine = engine
        self.battery = battery
