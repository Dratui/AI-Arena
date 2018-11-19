from src.games.games import Game
import random as rd

def ia_output(board,game):
    list_move_available=game.get_move_effective()
    if 2 in list_move_available:
        return(2)
    if 3 in list_move_available:
        return(3)
    else:
        return(rd.randint(0,1))




