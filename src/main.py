from aco.maze import Cell
from aco.data import load_data

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

    # Print cells relationship matrix
    for c in cells:
        cells[c].display()
