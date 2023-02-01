from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery

class Thovex(Car):
    def __init__(self, engine: CapuletEngine, battery: NubbinBattery):
        self.engine = engine
        self.battery = battery
