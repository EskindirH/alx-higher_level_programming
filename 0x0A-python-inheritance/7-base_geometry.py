#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """ Method not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
