# engine/sternmanengine.py
from engine.engine import Engine

# sternman engine implements Engine interface
class SternmanEngine(Engine):

   # we need the warning light status
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    # if the warning light is on, it needs to be serviced
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

''' 
from car import Car
class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
'''
