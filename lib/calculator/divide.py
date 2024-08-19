import numpy as np
from result import Err, Ok, Result

from lib.errors.error import Error


def divide(a: int | float, b: int | float) -> Result[int | float, Error]:
    """
    Divides two numbers and returns the result as a `Result` object.

    Args:
        a (int | float): The dividend.
        b (int | float): The divisor.

    Returns:
        Result[int | float, Error]: A `Result` object containing the result of the division if successful,
        or an `Error` object indicating that division by zero occurred.
    """
    if b == 0:
        return Err(Error.DIVISION_BY_ZERO)
    out: int = np.divide(a, b)
    return Ok(out)
