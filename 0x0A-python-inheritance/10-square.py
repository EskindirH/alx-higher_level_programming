#!/usr/bin/python3

"""

This module defines a square class
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Class Square that inherits from Rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square 

        Args:
            size: width of a square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()
