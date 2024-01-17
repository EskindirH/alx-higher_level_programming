#!/usr/bin/python3
"""

This module contains a class Rectangle

"""


from models.base import Base
class Rectangle(Base):
    """Class that inherits base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances

        Args:
            width: width of a rectangle
            height: height of a rectangle
            x: point on x
            y: point on y
            id: id of instance
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method

        Returns:
            width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """init width

        Args:
            value: value to init width

        Return:
            Void
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method

        Returns:
            No return
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Initializes height

        Args:
            value: init height

        Returns:
            Void
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method

        Returns:
            value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Init x
        Args:
            value: init x

        Returns:
            Void
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter Method

        Returns:
            void
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Inititializes y

        Args:
            value: init y

        Returns:
            void
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of rectangle

        Returns:
            area of the rectangle object
        """
        return self.width * self.height

    def display(self):
        """Displays a rectangle

        Returns:
            void
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method 

        Returns:
            no return
        """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh


    def update(self, *args, **kwargs):
        """Update method

        Args:
            args: unnamed args
            kwargs: named args

        Returns:
            void
        """

        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A dictionary with properties

        Returns:
            dictionary with properties
        """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res

