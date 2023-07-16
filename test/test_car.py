import unittest
from datetime import datetime
from car.car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestCarFactory(unittest.TestCase):

    # should be service due to last service date is more than 2 years ago
    def test_calliope_needs_service_due_to_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)  
        current_date = today
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # needs service due to mileage being more than 60000 and last service date being more than 2 years ago
    def test_glissade_needs_service_due_to_mileage(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)  
        current_date = today
        current_mileage = 60001
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # doesn't neeed service due to warning light being off and last service date being less than 2 years ago
    def test_palindrome_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 1)  
        current_date = today
        warning_light_on = False  
       
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)

        self.assertFalse(car.needs_service())

    # needs a service due to last service date being more than 4 years ago
    def test_rorschach_needs_service_due_to_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 5) 
        current_date = today
        current_mileage = 50000
        last_service_mileage = 30000
        
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # doesn't need service due to last service date being less than 4 years and millage being less than 30000
    def test_thovex_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 2)  
        current_date = today
        current_mileage = 20000
        last_service_mileage = 10000
        
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
