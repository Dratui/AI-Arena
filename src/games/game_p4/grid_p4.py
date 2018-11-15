import numpy as np


def create_grid(horizontal_size, vertical_size):
    """create an empty grid"""
    grid = []
    for i in range(vertical_size):
        grid.append([' ' for k in range(horizontal_size)])
    return grid


def display_grid(grid, size):
    """Convert grid to string to display it according to the parameters given by the player"""
    string = "|"
    for i in range(len(grid)):
        string += " "*int((size -1)/2) + str(i+1) +" "*int(np.ceil((size -1)/2)) + "|"
    string += "\n"
    for i in range(len(grid)):
        string += " "
        for j in range(len(grid[0])):
            string += "="*size + " "
        string += "\n|"
        for j in range(len(grid[0])):
            if grid[i][j] == " ":
                string += " "*size + "|"
            else:
                string += " "*int((size -1)/2) + ['O','X'][grid[i][j]] +" "*int(np.ceil((size -1)/2)) + "|"
        string += "\n"
    string += " "
    for i in range(len(grid[0])):
        string += "="*size + " "
    return string
