import random
from copy import deepcopy
import numpy as np


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
    """evolve the grid accordin'g to the direction asked by the player"""
    if direction == 1: #droite
        for i in range(4):
            line = board.read_row(i)[::-1]
            line = evolve_line(line)
            board.set_row(i, line[::-1])
    if direction == 3: #gauche
        for i in range(4):
            board.set_row(i, evolve_line(board.read_row(i)))
    if direction == 0: #haut
        for i in range(4):
            board.set_column(i, evolve_line(board.read_column(i)))
    if direction == 2: #bas
        for i in range(4):
            line = board.read_column(i)[::-1]
            line = evolve_line(line)
            board.set_column(i, line[::-1])

            #board.set_column(i, evolve_line(board.read_column(i)[::-1])[::-1])
    return board
def create_new_tile(board):
    """fill an empty tile with a 2 or a 4"""
    free_tiles = []
    for i in range(4):
        for j in range(4):
            if board.read_tile(i,j) == " ":
                free_tiles.append((i,j))
    k = random.randint(0,len(free_tiles)-1)
    coord = free_tiles[k]
    board.change_tile(coord[0],coord[1],random.randint(1,2)*2)

def move_possible(board):
    """return the list of the moves that are possible"""
    list = []
    for i in range(4):
        if board != make_a_move(deepcopy(board),i):
            list.append(i)
    return list


def is_over(board):
    """Check whether the grid is full or not"""
    if move_possible(board) == []:
        return True
    return False

def calc_score(board):
    sum = 0
    for i in board.get_all_tiles():
        if i!=' ':
            sum += int(int(i) * (np.log2(int(i))-1))
    return sum
