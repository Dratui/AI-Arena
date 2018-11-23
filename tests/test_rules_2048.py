from src.games.game_2048.rules_2048 import *
from pytest import *
from src.board import *
from src.games.game_2048.themes import THEMES
from src.games.games import *

def test_evolve_line():
    assert evolve_line([None for i in range(4)]) == [None for i in range(4)]
    assert evolve_line([None,4,4,8]) == [8,8,None,None]
    assert evolve_line([2, None, None, 2]) == [4,None,None,None]
    assert evolve_line([2, 4, None, 2]) == [2,4,2,None]

def test_make_a_move():
    game = init_game("2048")

    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]])
    game.make_a_move(3)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [4, None, None, None]]).get_all_tiles()
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]])
    game.make_a_move(1)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, 4]]).get_all_tiles()
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]])
    game.make_a_move(0)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[2, None, None, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]]).get_all_tiles()
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]])
    game.make_a_move(2)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]]).get_all_tiles()
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, 4, 2]])
    game.make_a_move(1)
    assert game.list_board[0].get_all_tiles() == generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, 2, 4, 2]]).get_all_tiles()

def test_is_over():
    game = init_game("2048")
    game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]])
    assert game.is_over()[0] == False
    game.list_board[0] = generate_board_from_list([[2*2**i,4*2**i,8*2**i,16*2**i] for i in range(4)])
    assert game.is_over()[0] == True

def test_calc_score():
	game = init_game("2048")
	game.list_board[0] = generate_board_from_list([[None, None, None, None], [None, None, None, None], [None, None, None, 2048], [2, 4, 16, 2]])
	assert calc_score(game.list_board, 0) == 2072
