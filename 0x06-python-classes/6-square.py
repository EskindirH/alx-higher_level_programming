#!/usr/bin/python3
class Square:
    """A class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Handles instantiation of private instances
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrives the value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrives the value of position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end='')
                print()
