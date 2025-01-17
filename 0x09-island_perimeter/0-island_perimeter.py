#!/usr/bin/python3
"""Defines a function to calculate the island perimeter."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list): A list of list of integers representing the island grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (above)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Subtract 2 for each adjacent land cell (left)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

