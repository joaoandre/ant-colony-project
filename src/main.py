import collections
import logging
import time

from aco.maze import Cell
from aco.data import load_data
from aco.ant import Ant
from aco.log_formatter import CustomFormatter
from matplotlib import pyplot as plt

from src.aco.visualization import generate_solution_plot, generate_convergence_plot

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fmt = '%(asctime)s | %(levelname)8s | %(message)s'

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(CustomFormatter(fmt))
logger.addHandler(stdout_handler)


if __name__ == "__main__":
    # load maze data from file
    maze_data = load_data("../resources/files/data.txt")

    # Get all available cell (the ones that are not walls)
    cells = {(i, j): Cell((i, j)) for i in range(len(maze_data)) for j in range(len(maze_data)) if
             maze_data[i][j] != '0'}

    dim = len(maze_data)
    entry = exit = (0, 0)

    for cell in cells:
        _x, _y = cell
        # Find entry cell
        if maze_data[_x][_y] == '2':
            entry = cell
        # Find exit cell

        if maze_data[_x][_y] == '3':
            exit = cell

        for (x, y) in [(_x, _y - 1), (_x, _y + 1), (_x - 1, _y), (_x + 1, _y)]:
            if 0 <= x < dim and 0 <= y < dim:
                if maze_data[x][y] != '0':
                    cells[cell].add_connected_cell(cells[(x, y)])

    # Set optimization parameters
    rho = 0.1
    alpha = 5
    n_ant = 50
    initial_pheromone = 0.1
    max_iterations = 50
    entry_cell = cells[entry]
    exit_cell = cells[exit]

    logger.debug("Setting initial feremone on cells")
    for cell in cells:
        cells[cell].set_pheromone(initial_pheromone)

    logger.debug("Creating Ants")
    time_data_points = []
    ants = [Ant() for _ in range(n_ant)]
    epoch = 0

    logger.debug("Starting Optimization")
    while epoch < max_iterations:
        begin = time.time()
        for ant in ants:
            logger.warning(f"{ant} is searching for an exit path")
            ant.reset()
            ant.get_path(entry_cell, exit_cell, alpha)

        logger.debug("Updating pheromone on cells")
        for cell in cells:
            cells[cell].update_pheromone(ants, rho)
        time_taken = time.time() - begin
        time_data_points.append((epoch, time_taken))
        logger.info(f"Interaction: {epoch}. Time taken: {time_taken}")
        if epoch == 0:
            paths = collections.Counter([tuple(ant.path) for ant in ants])
            solution = list(max(paths, key=paths.get))
            generate_solution_plot(solution, maze_data, entry, exit, "first_solution")
        epoch += 1

    logger.debug("Finished Optimization")

    # calculate the frequency of each path
    paths = collections.Counter([tuple(ant.path) for ant in ants])

    # find the path with the maximum frequency
    solution = list(max(paths, key=paths.get))

    generate_solution_plot(solution, maze_data, entry, exit, "final_solution")
    generate_convergence_plot(data_points=time_data_points)
