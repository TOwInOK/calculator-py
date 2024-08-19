import ast
import dataclasses

import numpy as np
from result import Err, Ok

from .divide import divide


@dataclasses.dataclass
class Calculator:
    """
    A class for performing calculations with an initial value.

    Attributes:
        value (int | float): The current value of the calculator.
    """

    value: int | float = 0

    def plus(self, number: int | float):
        """
        Adds the given number to the current value of the Calculator instance.

        Parameters:
            number (int | float): The number to be added to the current value.

        Returns:
            Calculator: The Calculator instance with the updated value.
        """
        self.value = np.add(self.value, number)
        return self

    def minus(self, number: int | float):
        """
        Subtracts the given number from the current value of the Calculator instance.

        Parameters:
            number (int | float): The number to be subtracted from the current value.

        Returns:
            Calculator: The Calculator instance with the updated value.
        """
        self.value = np.subtract(self.value, number)
        return self

    def multiply(self, number: int | float):
        """
        Multiplies the given number with the current value of the Calculator instance.

        Parameters:
            number (int | float): The number to be multiplied with the current value.

        Returns:
            Calculator: The Calculator instance with the updated value.
        """
        self.value = np.multiply(self.value, number)
        return self

    def divide(self, number: int | float):
        """
        Divides the current value of the Calculator instance by the given number.

        Parameters:
            number (int | float): The number to be divided into the current value.

        Returns:
            Calculator: The Calculator instance with the updated value.
        """
        division_result = divide(self.value, number)
        match division_result:
            case Ok(value):
                self.value = value
            case Err(error):
                raise (Exception(error))
        return self

    def calculate(self, value: str):
        """
        Calculates the result of an expression given as a string.

        Args:
            value (str): The expression to be evaluated.

        Returns:
            Calculator: The Calculator instance with the updated value.

        Raises:
            TypeError: If the expression cannot be parsed.

        This function takes a string expression as input and evaluates it using the Python `ast` module.
        It parses the expression using `ast.parse` and retrieves the root node of the expression tree.
        The `_eval` method is then called to evaluate the expression and update the value of the Calculator instance.
        The updated value is stored in the `self.value` attribute. Finally, the Calculator instance is returned.

        Note:
            The `calculate` method assumes that the expression is valid and can be parsed successfully.
            If the expression cannot be parsed, a `TypeError` is raised.
        """
        node = ast.parse(value, mode="eval").body
        self.value = self._eval(node)
        return self

    def _eval(self, node: ast.expr):
        """
        Evaluates the given abstract syntax tree (AST) expression and returns the result.

        Parameters:
            node (ast.expr): The AST expression to be evaluated.

        Returns:
            The result of the evaluated expression.

        Raises:
            TypeError: If the expression cannot be evaluated.
        """
        match node:
            case ast.Constant():
                return self.value + node.value
            case ast.BinOp() as bin_op:
                left = self._eval(bin_op.left)
                right = self._eval(bin_op.right)
                match bin_op.op:
                    case ast.Add():
                        return Calculator(left).plus(right).result()
                    case ast.Sub():
                        return Calculator(left).minus(right).result()
                    case ast.Mult():
                        return Calculator(left).multiply(right).result()
                    case ast.Div():
                        return Calculator(left).divide(right).result()
                    case _:
                        raise TypeError(bin_op.op)
            case _:
                raise TypeError(node)

    def result(self) -> int | float:
        """
        Returns the current value of the calculator.

        :return: An integer or a float representing the current value of the calculator.
        :rtype: int | float
        """
        return self.value
