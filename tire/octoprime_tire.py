from tire.tire import Tire
from utils import check_octoprime_tire_wear

class OctoprimeTire(Tire):
    
    # pass the tire wear array to the constructor
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    # check if the tire needs to be serviced
    def needs_service(self):
        return check_octoprime_tire_wear(self.tire_wear)