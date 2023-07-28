#!/usr/bin/env python3
"""
Python implementation of the pascals triangle
"""


def pascal_triangle(n):
    """
    This package implements the python triangle using python.
    The depth of the triangle is specified by the variable 'n'
    """

    triangle = []
    pascal_t = []
    for i in range(1, n + 1):
        row = [1] * (i)
        for j in range(2, i):
            row[j - 1] = pascal_t[i - 2][j - 2] + pascal_t[i - 2][j - 1]
        pascal_t.append(row)
    return pascal_t

print(pascal_triangle(5))
