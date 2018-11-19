from src.games.game_p4.rules_p4 import *
from pytest import *

from src.board import *

from src.games.games import *


def test_is_over():
    game = init_game("p4")
    game.list_board[0] = generate_board_from_list([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, ' ', ' ', 1]])
    assert game.is_over(0, player = 0) == False
    game.list_board[0] = generate_board_from_list([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, 0, 0, 0]])
    assert game.is_over(0,player = 0) == True
    game.list_board[0] = generate_board_from_list([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [1, 1, 1, 1]])
    assert game.is_over(0,player = 1) == True
    game.list_board[0] = generate_board_from_list([[0, ' ', ' ', ' '], [0, ' ', ' ', ' '], [0, ' ', ' ', ' '], [0, ' ', ' ', 1]])
    assert game.is_over(0,player = 0) == True


def test_make_a_move():
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, ' ', ' ', 1]], 1, 0) ==[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [1, ' ', ' ', ' '], [0, ' ', ' ', 1]]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [1, ' ', 0, 0]],0,2) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', 0, ' '], [1,' ',0,0]]
