#!/usr/bin/python3
class Square:
    """A class Square that defines a square
    """
    def __init__(self, size):
        """Initialize instances of a class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area
        """
        return (self.__size ** 2)
