from abc import ABC
from datetime import date

from battery.base import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    # needs service after 4 years
    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_date.year > 4
