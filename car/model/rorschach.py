from datetime import datetime



from car.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from datetime import date

class Rorschach(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        parts = {
            "engine": WilloughbyEngine(last_service_mileage, current_mileage),
            "battery": NubbinBattery(last_service_date, current_date)
        }
        super().__init__(parts)


''' from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False '''
