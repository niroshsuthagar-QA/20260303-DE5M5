import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(2,2)
        self.assertEqual(calculation.get_sum(), 4, "The answer is not 4!!")

    def test_diff(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')


if __name__ == "__main__":

    unittest.main()
