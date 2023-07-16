from battery.battery import Battery
from utils import add_years_to_date

# SpindlerBattery implements the Battery interface
class SpindlerBattery(Battery):

    # we need the last service date and current date to calculate the service threshold date
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

     # the service threshold date is 3 years after the last service date
    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False