#!/usr/bin/python3
class Square:
    """A class Square that defines a square
    """
    def __init__(self, size=0):
        """Instantiats instance of a class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrive value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints a square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
