import unittest
from intro_to_functions import main_functions


class FunctionTestCase(unittest.TestCase):
  def test_increase(self):
    self.assertEqual(main_functions.convert_to_months(12), 1)


if __name__ == "__main__":
    unittest.main()