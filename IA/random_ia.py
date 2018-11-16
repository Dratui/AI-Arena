from src.games.games import Game
from random import randint

def ia_output(board,game): # this ia randomize's its output
    return (game.map_move_to_input[randint(0,len(game.move_available))])



