from src.games.game_ttt.rules_ttt import *
from pytest import *
from src.board import *

def test_make_a_move():
    board = generate_board_from_list([[None for i in range(3)] for j in range(3)])
    assert generate_board_from_list([[None,1,None],[None,None,None],[None,None,None]]).get_all_tiles() == make_a_move(board,1,1).get_all_tiles()
    board = generate_board_from_list([[None for i in range(3)] for j in range(3)])
    assert generate_board_from_list([[None,None,None],[None,None,None],[None,None,0]]).get_all_tiles() == make_a_move(board,8,0).get_all_tiles()

def test_move_effective():
    board = generate_board_from_list([[None,1,None],[1,0,0],[None,1,None]])
    assert move_effective(board) == [0,2,6,8]
    board = generate_board_from_list([[1,1,0],[None,0,None],[1,None,None]])
    assert move_effective(board) == [3,5,7,8]


def test_is_over():
    board = generate_board_from_list([[None,1,None],[1,0,0],[None,1,None]])
    assert is_over(board) == False
    board = generate_board_from_list([[1 for i in range(3)] for j in range(3)])
    assert is_over(board) == True
    board = generate_board_from_list([[i+j*2 for i in range(3)] for j in range(3)])
    assert is_over(board) == True

def test_calc_score():
    list_board = [generate_board_from_list([[1,1,None],[1,0,0],[1,1,None]]),generate_board_from_list([[1,1,None],[1,0,0],[1,1,None]])]
    assert calc_score(list_board,1) == 1
    assert calc_score(list_board,0) == 0
