#!/usr/bin/python3
class Square:
    """A class Square that defines a square
    """
    def __init__(self, size=0):
        """Initialize instance of a class
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

    @property
    def size(self):
        """return size value
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
