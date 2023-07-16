from engine.engine import Engine

# willoughby engine implements Engine interface
class WilloughbyEngine(Engine):

    # we need the current mileage and the last service mileage
    def __init__(self,current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # if the current mileage minus the last service mileage is greater than 60000, it needs to be serviced
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

''' from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
'''
