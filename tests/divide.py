import unittest

from result import Err, Ok

from lib import Error, divide


class TestDivide(unittest.TestCase):
    def test_divide(self):
        """
        Tests the divide function to ensure it correctly divides two numbers and returns the result.

        Verifies that the result of dividing 10 by 2.5 is equal to 4.0.
        """
        self.assertEqual(divide(10, 2.5), Ok(4.0))

    def test_divide_by_zero(self):
        """
        Tests the divide function to ensure it correctly handles division by zero.

        Verifies that the result of dividing a number by zero returns an error with the DIVISION_BY_ZERO code.
        """
        self.assertEqual(divide(10, 0), Err(Error.DIVISION_BY_ZERO))


if __name__ == "__main__":
    unittest.main()
