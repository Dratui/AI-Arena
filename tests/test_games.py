from src.games.games import *
from pytest import *
from copy import deepcopy
from src.games.game_2048.rules_2048 import make_a_move as mk_mv


def test_game():
    game = Game()
    game.is_over_function = lambda x: 1
    game.list_board = [Board(4,4)]
    assert game.is_over()[0] == 1
    assert game.get_board() == Board(4,4)
    game.display_grid_function = lambda x: print(x)

def test_init_game():
    new_game = init_game("2048", players_number = 5)
    grid = deepcopy(new_game.list_board[0])
    new_game.make_a_move(0)
    assert mk_mv(grid,0) == new_game.list_board[0]
