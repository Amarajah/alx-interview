#!/usr/bin/python3
"""Pascal's triangle solution."""


def pascal_triangle(n):
    """Gives a list of lists representing the Pascal’s triangle of n"""
    """Initialize triangle with an empty list."""
    triangle = []

    """Loop through each row and initialize it with its value set as 1."""
    for i in range(1, n + 1):
        row = [1] * (i)
        """Iterate through the current row, except first and last elements."""
        for j in range(2, i):
            row[j - 1] = triangle[i - 2][j - 2] + triangle[i - 2][j - 1]
        """Append row."""
        triangle.append(row)
    return triangle
