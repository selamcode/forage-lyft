import unittest
from engine.capulet_engine import CapuletEngine

# lets test CapuletEngine

class TestCapuletEngine(unittest.TestCase):
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
        
if __name__ == '__main__':
    unittest.main()