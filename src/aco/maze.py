from dataclasses import dataclass
from typing import Tuple, List


class Cell:
    def __init__(self, coordinates, pheromone=0):
        self.coordinates = coordinates  # (x, y)
        self.pheromone = pheromone
        self.connected_cells = []

    def __str__(self):
        return f"{self.coordinates}"

    def add_connected_cell(self, other: "Cell"):
        if other not in self.connected_cells:
            self.connected_cells.append(other)

    def set_pheromone(self, pheromone):
        self.pheromone = pheromone

    def update_pheromone(self, ants, rho):
        self.pheromone = (1 - rho) * self.pheromone + sum(
            [1 / ant.get_path_length() for ant in ants if self in ant.path]
        )

    def display(self):
        print(f"{self.coordinates}: {[c.coordinates for c in self.connected_cells]}")
