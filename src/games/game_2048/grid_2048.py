import random
import numpy as np
from src.games.game_2048.themes import THEMES

def create_grid():
    """create an empty grid"""
    grid = []
    for i in range(0,4):
        grid.append([' ',' ',' ', ' '])
    return grid

def init_grid():
    """create an empty grid and fill one tile with 2 and another with 4"""
    grid = create_grid()
    i2,j2 = random.randint(0,3),random.randint(0,3)
    grid[i2][j2] = 2
    i4,j4 = random.randint(0,3),random.randint(0,3)
    while i2 == i4 and j2 == j4:
        i4,j4 = random.randint(0,3),random.randint(0,3)
    grid[i4][j4] = 4
    return grid

def display_grid(grid, player_size = 5, theme_number = 0):
    """Convert grid to string to display it according to the parameters given by the player"""
    theme = THEMES[theme_number]
    theme_size_calc = theme_size(theme)
    size = max(theme_size_calc, player_size)
    string = ""
    for i in range(4):
        string += " "
        for j in range(4):
            string += "="*size + " "
        string += "\n|"
        for j in range(4):
            if grid[i][j] == " ":
                string += " "*size + "|"
            else:
                number_size = elem_to_string_size(theme[grid[i][j]])
                string += " "*int((size -number_size)/2) + theme[grid[i][j]] +" "*int(np.ceil((size -number_size)/2)) + "|"
        string += "\n"
    string += " "
    for i in range(4):
        string += "="*size + " "
    return string

def theme_size(theme):
    """compute the size of the biggest element of the theme"""
    max = 0
    for case in range(1,14):
        if max < elem_to_string_size(theme[2**case]):
            max = elem_to_string_size(theme[2**case])
    return max

def elem_to_string_size(n):
    """return the number of caracters needed to print a given element (int or str)"""
    if type(n) == type("str"):
        return len(n)
    return int(np.ceil(np.log10(n)))
