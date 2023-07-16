from serviceable import Serviceable

# car implements Serviceable interface
class Car(Serviceable):

    # in the future, we can add more parts to the car (Engine, Battery, Tire, Transmission, etc.)
    def __init__(self, parts:dict):
        self.parts = parts
        
    # for each part (engine, battery, etc.), check if it needs to be serviced using the needs_service method
    def needs_service(self):
        for part in self.parts.values():
            if part.needs_service():
                return True
        return False