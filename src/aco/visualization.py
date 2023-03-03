import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')  # !IMPORTANT


def generate_solution_plot(solution, maze_data, entry, exit, name="final_solution"):
    X = []
    Y = []
    for i in range(len(solution)):
        X.append(solution[i].coordinates[0])
        Y.append(solution[i].coordinates[1])
    data = []
    for i in range(len(maze_data)):
        newList = []
        for j in range(len(maze_data)):
            if maze_data[i][j] == '1' or maze_data[i][j] == '2' or maze_data[i][j] == '3':
                newList.append(1)
            else:
                newList.append(0)
        data.append(newList)
    plt.figure(figsize=(7, 7))
    plt.title("Path from " + str(entry) + " To " + str(exit))
    plt.imshow(data, cmap='gray')
    plt.plot(Y, X, color='red')
    plt.scatter([entry[1]], [entry[0]], color='green')
    plt.scatter([exit[1]], [exit[0]], color='blue')
    plt.savefig(f'../resources/imgs/{name}.png')


def generate_convergence_plot(data_points):
    plt.figure(figsize=(7, 7))
    plt.title("Convergence")
    plt.plot(*zip(*data_points), color='blue')
    plt.savefig(f'../resources/imgs/convergence.png')
