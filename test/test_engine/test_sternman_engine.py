import unittest
from engine.sternman_engine import SternmanEngine

# lets test SternmanEngine

class TestSternmanEngine(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main()