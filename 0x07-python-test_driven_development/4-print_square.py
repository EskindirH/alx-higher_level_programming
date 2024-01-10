#!/usr/bin/python3
"""

This module contains a function that prints a square with the character #.

"""

def print_square(size):
    """ Funtion that prints a square with the character #.

    Args:
        size: size of the square.

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer
                   if size is a float and is less than 0
        ValueError: if size is less than 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("#" * size)
