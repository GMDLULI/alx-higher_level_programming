#!/usr/bin/python3

"""
    this module deivdes all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
         ZeroDivisionError: If div is zero
      """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mesg_type = 'matrix must be a matrix (list of lists) of integers/floats'

    if not matrix or not isinstance(matrix, list):
        raise TypeError(mesg_type)

    len_e = 0
    mesg_size = 'Each row of the matrix must have the same size'

    for elms in matrix:
        if not elms or not isinstance(elms, list):
            raise TypeError(mesg_type)

        if len_e != 0 and len(elms) != len_e:
            raise TypeError(mesg_size)

        for num in elms:
            if not type(num) in (int, float):
                raise TypeError(mesg_type)

        len_e = len(elms)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
