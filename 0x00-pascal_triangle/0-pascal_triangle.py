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
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
