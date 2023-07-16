import unittest
from datetime import date
from utils import add_years_to_date

# util test class
class UtilsTest(unittest.TestCase):

    # Testing the `add_years_to_date` function inside utils.py
    def test_add_years_to_date(self):
        original_date = date(2020, 1, 1)  
        years_to_add = 3  
        expected_date = date(2023, 1, 1)  
        result_date = add_years_to_date(original_date, years_to_add)
        self.assertEqual(expected_date, result_date)

    # Testing the `add_years_to_date` function inside utils.py
    def test_add_zero_years(self):
        original_date = date(2020, 1, 1)  
        years_to_add = 0  
        expected_date = date(2020, 1, 1)
        result_date = add_years_to_date(original_date, years_to_add)
        self.assertEqual(expected_date, result_date)

if __name__ == '__main__':
    unittest.main()
