from abc import ABC

from battery.base import Battery


class SpliderBattery(Battery, ABC):
    def __init__(self, current_date, last_service_charge):
        self.current_date = current_date
        self.last_service_charge = last_service_charge

    # needs service after 2 years
    def needs_service(self) -> bool:
        return self.current_date - self.last_service_charge > 2