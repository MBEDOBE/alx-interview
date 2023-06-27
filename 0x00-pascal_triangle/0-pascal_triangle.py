#!/usr/bin/python3
"""Pascal triangle"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given n value.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.

    """
    if n <= 0:
        # Return an empty list if n <= 0
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i-1]

        for j in range(1, i):
            # Compute each element in the current row
            element = prev_row[j-1] + prev_row[j]
            row.append(element)

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
