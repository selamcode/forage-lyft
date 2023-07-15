from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, parts:dict):
        self.parts = parts

    def needs_service(self):
        for part in self.parts.values():
            if part.needs_service():
                return True
        return False

''' class Car(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
'''
