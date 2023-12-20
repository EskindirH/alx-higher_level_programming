#!/usr/bin/python3
class Square:
    """A class that defines square by size
    """
    def __init__(self, size):
        """Initialize the square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
