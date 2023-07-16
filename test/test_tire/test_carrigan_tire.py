import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):

    # it should be serviced because the last tire wear is 1
    def test_carrigan_tire_should_be_serviced(self):
        tire_wear = [0.5, 0.5, 0.5, 1]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertTrue(carrigan_tire.needs_service())

     # it shouldn't be serviced because all tire wears are less than 0.9
    def test_carrigan_tire_should_not_be_serviced(self):
        tire_wear = [0.5, 0.5, 0.5, 0.5]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertFalse(carrigan_tire.needs_service())

if __name__ == '__main__':
    unittest.main()