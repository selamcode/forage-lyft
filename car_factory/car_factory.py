from car.car import Car
from car.model.calliope import Calliope
from car.model.glissade import Glissade
from car.model.palindrome import Palindrome
from car.model.rorschach import Rorschach
from car.model.thovex import Thovex
from datetime import date

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Palindrome(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
