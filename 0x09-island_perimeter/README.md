# 0x09. Island Perimeter

Island Perimeter Calculator

This Python script calculates the perimeter of an island represented by a grid. The grid consists of cells, where:

- `0` represents water
- `1` represents land

Each cell is square and connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is only one island (or nothing). The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).


#!/usr/bin/python3
"""
Island Perimeter: returns the perimeter of the island  described in grid
"""


def island_perimeter(grid):
    """  island perimeter function"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides
                # Check adjacent cells (up, down, left, right) and subtract if neighboring land
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
