import unittest
from engine.willoughby_engine import WilloughbyEngine

# lets test WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
     # It has been less than 60,000 miles, so it shouldn't be serviced
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())

    # It has been exactly 60,000 miles, so it shouldn't be serviced
    def test_willoughby_engine_on_borderline_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())

     # It has been more than 60,000 miles, so it should be serviced
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60002
        last_service_mileage = 0
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())
if __name__ == '__main__':
    unittest.main()