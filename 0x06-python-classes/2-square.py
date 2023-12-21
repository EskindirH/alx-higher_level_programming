#!/usr/bin/python3

"""Class that defines square by size."""

class Square:
    """A class that defines square by size."""

    def __init__(self, size=0):
        """Initialize the square instance.

        Args:
            size (int): The size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
