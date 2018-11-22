from src.games.games import Game
import random

def ai_output(board, game):# this ai randomize's its output
    return (random.choice(game.get_move_effective()))



