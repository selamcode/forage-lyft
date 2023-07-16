import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import date

# test our Spindler battery
class TestSpindlerBattery(unittest.TestCase):

    # It has been 4 years, more than 3 years, so it should be serviced
    def test_spindler_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        current_date = today
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    # It has been 3 years not more, so it shouldn't be serviced
    def test_spindler_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_date = today
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
