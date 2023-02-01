from abc import ABC
from datetime import date

from battery.base import Battery


class SpliderBattery(Battery, ABC):
    def __init__(self, current_date: date, last_service_charge: date):
        self.current_date = current_date
        self.last_service_charge = last_service_charge

    # needs service after 2 years
    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_charge.year > 3