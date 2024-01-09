#!/usr/bin/python3
"""

This module contains a function that prints a message.

"""

def say_my_name(first_name, last_name=""):
    """ Function that prints a message

    Args:
        first_name: string argument
        last_name: string argument

    Returns:
        Void
    Raises:
        TypeError: If first_name/last_name is not of type string

    """

    if not first_name isinstance(str):
        raise TypeError("first_name must be a string")

    if not last_name isinstance(str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
