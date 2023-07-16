from tire.tire import Tire
from utils import check_carrigan_tire_wear

class CarriganTire(Tire):
    
    # pass the tire wear array to the constructor
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    # check if the tire needs to be serviced
    def needs_service(self):
        return check_carrigan_tire_wear(self.tire_wear)
