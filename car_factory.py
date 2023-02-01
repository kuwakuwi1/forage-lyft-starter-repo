from car import Car

from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.splider_battery import SpliderBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpliderBattery(current_date, last_service_date))

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpliderBattery(current_date, last_service_date))

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpliderBattery(current_date, last_service_date))

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car: 
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))