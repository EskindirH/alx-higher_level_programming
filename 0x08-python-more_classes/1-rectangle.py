#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """A Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initializes an instance of a Rectangle class.

        Args:
            width (int): Width of a rectangel.
            height (int): height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of a rectangel.

        Args:
            value: width value

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height

        Returns:
            height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
