#!/usr/bin/python3
"""Pascal's triangle solution."""


def pascal_triangle(n):
    """returns a list of lists of integers."""
    """If n<= 0, return an empty list."""
    if (n <= 0):
        return []
    """Initialize the triangle variable."""
    triangle = [[1]]

    """Loop through the triangle."""
    for i in range(1, n):
        prev_row = triangle[i - 1]
        curr_row = [1]

        """Append elements."""
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

        """Return triangle as result"""
        return triangle
