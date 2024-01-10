#!/usr/bin/python3

"""

This module contains a rebelion class that invert == and != operators

"""


class MyInt(int):
    """ Class that inherits from class int"""

    def __eq__(self, other):
        """ Method that returns != check """
        return super().__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return super().__eq__(self, other)
