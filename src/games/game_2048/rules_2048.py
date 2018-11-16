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

def make_a_move(board,direction, player = 0):
    """evolve the grid according to the direction asked by the player"""
    if direction == 1: #droite
        for i in range(4):
            line = board.read_row(i)[::-1]
            line = evolve_line(line)
            board.set_row(i, line[::-1])
    if direction == 3: #gauche
        for i in range(4):
            board.set_row(i, evolve_line(board.read_row(i)))
    if direction == 0: #haut
        board.transpose_grid_anticlockwise()
        for i in range(4):
            board.set_row(i, evolve_line(board.read_row(i)))
        board.transpose_grid_clockwise()
    if direction == 2: #bas
        board.transpose_grid_clockwise()
        for i in range(4):
            board.set_row(i, evolve_line(board.read_row(i)))
        board.transpose_grid_anticlockwise()
    return grid

def create_new_tile(grid):
    """fill an empty tile with a 2 or a 4"""
    free_tiles = []
    for i in range(4):
        for j in range(4):
            if board.read_tile(i,j) == " ":
                free_tiles.append((i,j))
    k = random.randint(0,len(free_tiles)-1)
    coord = free_tiles[k]
    board.change_tile(i,j,random.randint(1,2)*2)
    return grid

def move_possible(board):
    """return the list of the moves that are possible"""
    list = []
    for i in range(4):
        board_copy = board
        if board != make_a_move(board,i):
            list.append(i)
    return list


def is_over(board):
    """Check whether the grid is full or not"""
    if move_possible(board) == []:
        return True
    return False
