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
