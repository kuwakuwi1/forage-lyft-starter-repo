from car import Car

from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.splider_battery import SpliderBattery
from battery.nubbin_battery import NubbinBattery
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(CapuletEngine(current_mileage, last_service_mileage), SpliderBattery(current_date, last_service_date))

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(WilloughbyEngine(current_mileage, last_service_mileage), SpliderBattery(current_date, last_service_date))

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Palindrome(SternmanEngine(warning_light_on), SpliderBattery(current_date, last_service_date))

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car: 
        return Thovex(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))