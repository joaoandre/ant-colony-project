from random import random
import names


class Ant:
    def __init__(self):
        self.path = []
        self.name = names.get_first_name()

    def __repr__(self):
        return f"Ant<{self.name}>"

    def get_path_length(self):
        return len(self.path)

    def reset(self):
        self.path = []

    def get_path(self, entry_cell, exit_cell, alpha):
        # Adding entrance to the route
        self.path.append(entry_cell)
        # Check if the entrance and exit is the same
        while self.path[-1] != exit_cell:
            # Check if we didn't end up at the same point of entrance
            if self.path[-1] != entry_cell:
                if len(self.path[-1].connected_cells) > 1:
                    # Add cells adjacent to the last cell of the path to the options, except for the second-last cell
                    # of the path. 
                    options = [cell for cell in self.path[-1].connected_cells if cell != self.path[-2]]
                else:
                    options = self.path[-1].connected_cells
            else:
                options = self.path[-1].connected_cells

            total_pheromone = 0
            # Calculate the Total pheromone spread by ants
            for connected_cell in options:
                total_pheromone += (connected_cell.pheromone ** alpha)

            # Calculate the total pheromone available on the cells in options
            total_pheromone = sum([c.pheromone ** alpha for c in options])

            # Calculating list with cumulative probabilities for roulette wheel selection
            cumulative_prob = []
            accumulator = 0
            for c in options:
                accumulator += (c.pheromone ** alpha) / total_pheromone
                cumulative_prob.append(accumulator)

            # Selecting the next cell
            random_num = random()
            for i in range(len(cumulative_prob)):
                if random_num <= cumulative_prob[i]:
                    cell_index = i
                    break

            # Adding the selected cell to the path
            self.path.append(options[cell_index])

            # Removing cycles
            for i in range(len(self.path) - 1):
                for j in range(len(self.path) - 1, i, -1):
                    if self.path[i] == self.path[j]:
                        del self.path[i:j]
                        break
