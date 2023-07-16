from car.car import Car # from car module import Car class
from datetime import date # from datetime module import date class
from engine.capulet_engine import CapuletEngine # from engine module import CapuletEngine class
from engine.willoughby_engine import WilloughbyEngine # from engine module import WilloughbyEngine class
from engine.sternman_engine import SternmanEngine # from engine module import SternmanEngine class
from battery.spindler_battery import SpindlerBattery # from battery module import SpindlerBattery class
from battery.nubbin_battery import NubbinBattery # from battery module import NubbinBattery class


''' This is where we create all our car models, 
letter we don't need to instantiate them in the main.py file '''

class CarFactory:

    # creating calliope car model
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        parts = {
            "engine": CapuletEngine(last_service_mileage, current_mileage),
            "battery": SpindlerBattery( current_date, last_service_date)
        }
        car = Car(parts)
        return car

    # creating glissade car model
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        parts = {
            "engine": WilloughbyEngine(last_service_mileage, current_mileage),
            "battery": SpindlerBattery(current_date, last_service_date)
        }
        car = Car(parts)
        return car

    # creating palindrom car model
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        parts = {
            "engine": SternmanEngine(warning_light_on),
            "battery": SpindlerBattery(current_date,last_service_date)
        }
        car = Car(parts)
        return car

    # creating rorschach car model
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        parts = {
            "engine": WilloughbyEngine(last_service_mileage, current_mileage),
            "battery": NubbinBattery(current_date, last_service_date)
        }
        car = Car(parts)
        return car

    # creating thovex car model
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        parts = {
            "engine": CapuletEngine(last_service_mileage, current_mileage),
            "battery": NubbinBattery(current_date, last_service_date)
        }
        car = Car(parts)
        return car
