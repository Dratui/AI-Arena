import random
import numpy as np
from src.games.game_2048.themes import THEMES

def init_board(board):
    """create an empty grid and fill one tile with 2 and another with 4"""
    i2,j2 = random.randint(0,3),random.randint(0,3)
    board.change_tile(i2,j2,2)
    i4,j4 = random.randint(0,3),random.randint(0,3)
    while i2 == i4 and j2 == j4:
        i4,j4 = random.randint(0,3),random.randint(0,3)
    board.change_tile(i4,j4,4)
    return board
