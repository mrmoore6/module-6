import unittest
from more_functions import string_functions

class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertTrue("Mike,Mike,Mike,Mike", string_functions.multiply_string(4, "Mike"))



if __name__ == '__main__':
    unittest.main()
