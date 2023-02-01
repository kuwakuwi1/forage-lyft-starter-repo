from datetime import date
import unittest
from battery.nubbin_battery import NubbinBattery

from battery.splider_battery import SpliderBattery

class TestSpliderBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2019-01-31") # 4 years ago

        battery = SpliderBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2020-01-31") # 3 years ago

        battery = SpliderBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2018-01-31") # 5 years ago

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.fromisoformat("2023-01-31")
        last_service_date = date.fromisoformat("2020-01-31") # 4 years ago

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()