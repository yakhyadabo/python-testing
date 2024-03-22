import unittest

from src.numbers.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_inc(self):
        calculator = Calculator()
        ans = calculator.inc(5)
        self.assertEqual(ans, 6)

    def test_sum(self):
        calculator = Calculator()
        ans = calculator.sum(10,11)
        self.assertEqual(ans, 21)

if __name__ == '__main__':
    unittest.main()
