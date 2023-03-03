from typing import List


def load_data(filepath: str) -> List:
    """"Load Maze Data
    The data is a 2D matrix filled with numbers, where the number representation is as follows:
    0: Represents a wall on the maze
    1: Represents an empty cell on the maze
    2: Represents the starting point for the ants
    3: Represents the exit point for the ants
    """
    with open(filepath) as f:
        return [row.split() for row in f]
