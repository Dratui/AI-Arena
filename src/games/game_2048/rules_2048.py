import random
from copy import deepcopy
def evolve_line(line):
    """evolve a line as if it yas pushed to the left"""
    for i in range(4):
        for k in range(i+1,4):
            if line[i] == line[k] and line[i] != " ":
                line[i],line[k] = 2*line[k]," "
                break
            if line[k]!=line[i] and line[k] != " ":
                break
    for i in range(4):
        if line[i] == " ":
            for k in range(i,4):
                if line[k] != " ":
                    line[i],line[k] = line[k]," "
                    break
    return line

def make_a_move(grid,direction):
    """evolve the grid according to the direction asked by the player"""
    if direction == 0:
        for i in range(4):
            grid[i] = evolve_line(grid[i][::-1])[::-1]
            print()
    if direction == 1:
        for i in range(4):
            grid[i] = evolve_line(grid[i])
    if direction == 2:
        for i in range(4):
            line = []
            for j in range(4):
                line.append(grid[j][i])
            line = evolve_line(line)
            for j in range(4):
                grid[j][i] = line[j]
    if direction == 3:
        for i in range(4):
            line = []
            for j in range(4):
                line.append(grid[3-j][i])
            line = evolve_line(line)
            for j in range(4):
                grid[3-j][i] = line[j]
    return grid

def create_new_tile(grid):
    """fill an empty tile with a 2 or a 4"""
    free_tiles = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == " ":
                free_tiles.append((i,j))
    k = random.randint(0,len(free_tiles)-1)
    coord = free_tiles[k]
    grid[coord[0]][coord[1]] = random.randint(1,2)*2
    return grid

def is_over(grid):
    """Check whether the grid is full or not"""
    grid_copy = deepcopy(grid)
    for i in range(4):
        if grid_copy != make_a_move(grid,i):
            return False
    return True
