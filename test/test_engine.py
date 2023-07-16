import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):

    ''' Let's test CapuletEngine '''

    # It has been more than 30,000 miles, so it should be serviced
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    # It has been less than 30,000 miles, so it shouldn't be serviced
    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage,)
        self.assertFalse(capulet_engine.needs_service())

    # It has been exactly 30,000 miles, so it shouldn't be serviced
    def test_capulet_engine_on_borderline_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())

    ''' Let's test SternmanEngine '''

    # Warning light is on, so it should be serviced
    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertTrue(sternman_engine.needs_service())

    # Warning light is off, so it shouldn't be serviced
    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_on = False
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertFalse(sternman_engine.needs_service())

    ''' Let's test WilloughbyEngine '''

   

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
