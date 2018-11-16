from src.games.games import Game
from random import randint

def ia_output(board,game): #cette IA fait un output random des differentes entrées possibles
    return randint(0,len(game.move_available()))



