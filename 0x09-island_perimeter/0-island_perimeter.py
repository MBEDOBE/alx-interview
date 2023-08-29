#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
