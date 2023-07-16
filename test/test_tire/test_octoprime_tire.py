import unittest
from tire.octoprime_tire import OctoprimeTire
from utils import check_octoprime_tire_wear

class TestOctoprimeTire(unittest.TestCase):
        
        # it should be serviced because the sum of the tire wear is greater than or equal to 3
        def test_octoprime_tire_should_be_serviced(self):
            tire_wear = [1.5, 1.5, 0.5, 0.5]
            octoprime_tire = OctoprimeTire(tire_wear)
            self.assertTrue(octoprime_tire.needs_service())
        
        # it shouldn't be serviced because the sum of the tire wear is less than 3
        def test_octoprime_tire_should_not_be_serviced(self):
            tire_wear = [0.5, 0.5, 0.5, 0]
            octoprime_tire = OctoprimeTire(tire_wear)
            self.assertFalse(octoprime_tire.needs_service())

if __name__ == '__main__':
    unittest.main()