from engine.engine import Engine

# capulet engine implements Engine interface
class CapuletEngine(Engine):

    # we need the last service mileage and the current mileage
    def __init__(self,current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        

    # if the current mileage minus the last service mileage is greater than 30000, rit needs to be serviced
    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 30000

