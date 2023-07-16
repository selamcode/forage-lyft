import unittest
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import date

# Let's test our batteries
class TestBattery(unittest.TestCase):

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

    # It has been 1 year, so it shouldn't be serviced
    def test_nubbin_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_date = today
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())


    # Let's test our Spindler battery

    # It has been 3 years, more than 2 years, so it should be serviced
    def test_spindler_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_date = today
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    # It has been 1 years, so it shouldn't be serviced
    def test_spindler_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_date = today
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())

    # It has been 2 years, so it shouldn't be serviced
    def test_spindler_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        current_date = today
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
