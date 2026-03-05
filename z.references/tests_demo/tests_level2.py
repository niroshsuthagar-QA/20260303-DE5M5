import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.myCalc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.myCalc.get_sum(), 10, "The answer is not 4!!")

    def test_diff(self):
        self.assertEqual(self.myCalc.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.myCalc.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.myCalc.get_quotient(), 4, 'The quotient is wrong.')


if __name__ == "__main__":

    unittest.main()
