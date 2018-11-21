from src.games.games import Game
from src.board import Board
import time

def ai_output(board,game):
    board.input=None
    while board.input==None or game.map_input_to_move[board.input] not in game.get_move_effective():
        time.sleep(0.5)
    return(game.map_input_to_move[board.input])


