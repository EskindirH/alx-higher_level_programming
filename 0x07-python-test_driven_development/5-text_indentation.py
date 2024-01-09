#!/usr/bin/python3
"""

This module contains a function that prints a text with 2 new lines after ".?:" chars

"""

def text_indentation(text):
    """ function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        Void

    Raises:
        TypeError: If text is not string.

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        lst_txt = s.split(d)
        s = ""
        for i in lst_txt:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
