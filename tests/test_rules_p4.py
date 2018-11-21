from src.games.game_p4.rules_p4 import *
from pytest import *

from src.board import *

from src.games.games import *


def test_is_over():
    game = init_game("p4")
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [0, None, None, 1]])
    assert game.is_over()[0] == False
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [0, 0, 0, 0]])
    assert game.is_over()[0] == True
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [1, 1, 1, 1]])
    assert game.is_over()[0] == True
    game.list_board[0] = generate_board_from_list([[0, None, None, None], [0, None, None, None], [0, None, None, None], [0, None, None, 1]])
    assert game.is_over()[0] == True


def test_make_a_move():
    game = init_game("p4")
    game.list_board[1] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [0, None, None, 1]])
    game.player_playing = 1
    game.make_a_move(0)
    assert game.list_board[1].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [1, None, None, None], [0, None, None, 1]]).get_all_tiles()
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [1, None, 0, 0]])
    game.player_playing = 0
    game.make_a_move(2)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, 0, None], [1,None,0,0]]).get_all_tiles()
