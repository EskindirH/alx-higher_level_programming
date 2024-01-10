#!/usr/bin/python3
"""

This module contains a function.
It divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """ Function that divide elements of matrix.

    Args:
        matrix: list of lists
        div: divides elements of matrix

    Returns:
        A new matrix

    Raises:
        ZeroDivisionError: Raised when div equals to zero

        TypeError: If elements of matrix are not integer/float
                   If matrix is not list of lists
                   If row of matrix has differnt size
                   If div is not integer or float


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_elt = 0
    err_size = "Each row of the matrix must have the same size"
    err_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_type)

    for elts in matrix:
        if not elts or not isinstance(elts, list):
            raise TypeError(err_type)

        if len_elt != 0 and len(elts) != len_elt:
            raise TypeError(err_size)

        for num in elts:
            if not type(num) in (int, float):
                raise TypeError(err_type)

        len_elt = len(elts)

    new_mat = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (new_mat)
