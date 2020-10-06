import unittest
from more_functions import validate_input_in_functions as valid_function

class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Math: 0%", valid_function.score_input("Math"))

    def test_score_input_test_valid(self):
        self.assertEqual(True, False)

    def test_score_input_test_below_range(self):
        self.assertEqual(True, False)

    def test_score_input_test_above_range(self):
        self.assertEqual(True, False)

    def test_score_input_test_non_numeric(self):
        self.assertEqual(True, False)

    def test_score_input_test_invalid_message(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
