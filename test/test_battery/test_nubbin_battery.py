import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import date

# test our Nubbin battery
class TestNubbinBattery(unittest.TestCase):

    # It has been 5 years, so it should be serviced
    def test_nubbin_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_date = today
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

    # It has been 4 years but not more, so it shouldn't be serviced
    def test_nubbin_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        current_date = today
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

if __name__ == '__main__':
    unittest.main()