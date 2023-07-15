
from car.car import Car
from engine.capulet_engine import  CapuletEngine
from battery.spindler_battery import SpindlerBattery
from datetime import date

class Calliope(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        parts = {
            "engine": CapuletEngine(last_service_mileage, current_mileage),
            "battery": SpindlerBattery(last_service_date, current_date)
        }
        super().__init__(parts)

        
        
''' from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False'''
