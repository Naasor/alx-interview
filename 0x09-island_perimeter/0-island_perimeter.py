#!/usr/bin/python3
"""
This module contains the island_perimeter function that calculates the perimeter
of an island represented in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check all four directions
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1
    return perimeter
