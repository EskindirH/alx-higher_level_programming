#!/usr/bin/python3

"""

This module defines a class Rectangle

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class that inherits BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
