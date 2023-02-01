from car import Car
from engine.sternman_engine import SternmanEngine
from battery.splider_battery import SpliderBattery

class Palindrome(Car):
    def __init__(self, engine: SternmanEngine, battery: SpliderBattery):
        self.engine = engine
        self.battery = battery
