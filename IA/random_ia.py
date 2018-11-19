from src.games.games import Game
import random

def ia_output(board,game):# this ia randomize's its output
    return (random.choice(game.get_move_effective()))



