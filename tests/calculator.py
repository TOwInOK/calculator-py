import unittest

from lib import Calculator, Error


class TestCalculator(unittest.TestCase):
    """
    Test cases for the Calculator class.
    """

    def test_initial_value(self):
        """
        Test that the initial value of the calculator is 0.
        """
        calc = Calculator()
        self.assertEqual(calc.result(), 0)

    def test_addition(self):
        """
        Test that the addition works correctly.
        """
        calc = Calculator(5).plus(3)
        self.assertEqual(calc.result(), 8)

    def test_subtraction(self):
        """
        Test that the subtraction works correctly.
        """
        calc = Calculator(5).minus(3).result()
        self.assertEqual(calc, 2)

    def test_multiplication(self):
        """
        Test that the multiplication works correctly.
        """
        calc = Calculator(5).multiply(3).result()
        self.assertEqual(calc, 15)

    def test_division(self):
        """
        Test that the division works correctly.
        """
        calc = Calculator(10).divide(2).result()
        self.assertEqual(calc, 5)

    def test_division_by_zero(self):
        """
        Test that the division by zero raises an exception.
        """
        with self.assertRaises(Exception) as context:
            Calculator().divide(0)
        self.assertEqual(context.exception.args[0], Error.DIVISION_BY_ZERO)

    def test_complex_expression(self):
        """
        Test that a complex expression works correctly.
        """
        result = Calculator().calculate("(10.2+5)*2").minus(5).result()
        self.assertEqual(result, 25.4)

    def test_invalid_expression(self):
        """
        Test that an invalid expression raises an exception.
        """
        with self.assertRaises(Exception) as context:
            Calculator().calculate("10/0")
        self.assertEqual(context.exception.args[0], Error.DIVISION_BY_ZERO)

    def test_result(self):
        """
        Test that the result of the calculator is correct.
        """
        calc = Calculator(10).result()
        self.assertEqual(calc, 10)


if __name__ == "__main__":
    unittest.main()
