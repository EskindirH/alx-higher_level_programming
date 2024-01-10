#!/usr/bin/python3
"""

This module contains function to add numbers.

"""

def add_integer(a, b=98):
    """ Function that adds 2 integers.

    Args:
        a: first number
        b: second number

    Returns:
        The sum of two numbers.

    Raises:
        TypeError: a must be an integer and/or b must be an integer.

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
