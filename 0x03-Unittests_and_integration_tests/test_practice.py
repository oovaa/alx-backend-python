import unittest


class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        # self.assertEqual(str(context.exception), "Cannot divide by zero!")

    def tearDown(self):
        del self.calc


if __name__ == '__main__':
    unittest.main()
