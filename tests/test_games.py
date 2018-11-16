from src.games.games import *
from pytest import *

def test_game():
    game = Game()
    game.is_over_function = lambda x: 1
    assert game.is_over(1) == 1
    game.list_board = [[[" " for j in range(4)] for i in range(4)]]
    assert game.get_grid() == [[" " for j in range(4)] for i in range(4)]
    game.display_grid_function = lambda x: print(x)
