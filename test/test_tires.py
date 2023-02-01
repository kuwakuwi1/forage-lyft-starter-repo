import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase): 
    def test_tires_should_be_serviced(self):
        wear_sensors = [0, 0, 0, 0.9]

        tires = CarriganTires(wear_sensors)
        self.assertTrue(tires.needs_service())
    
    def test_tires_should_not_be_serviced(self):
        wear_sensors = [0.8, 0, 0, 0]

        tires = CarriganTires(wear_sensors)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear_sensors = [1, 0.9, 0.1, 1] # 3.0

        tires = OctoprimeTires(wear_sensors)
        self.assertTrue(tires.needs_service())
    
    def test_tires_should_not_be_serviced(self):
        wear_sensors = [0.2, 0.8, 0.3, 0.6] # 2.9

        tires = OctoprimeTires(wear_sensors)
        self.assertFalse(tires.needs_service())