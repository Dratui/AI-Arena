from src.games.game_2048.rules_2048 import *
from pytest import *
from src.board import *
from src.games.game_2048.themes import THEMES
from src.games.games import *

def test_evolve_line():
    assert evolve_line([" " for i in range(4)]) == [" " for i in range(4)]
    assert evolve_line([" ",4,4,8]) == [8,8," "," "]
    assert evolve_line([2, ' ', ' ', 2]) == [4,' ',' ',' ']
    assert evolve_line([2, 4, ' ', 2]) == [2,4,2,' ']

def test_make_a_move():
    game = init_game("2048")

    game.list_board[0] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    game.make_a_move(3)
    assert game.list_board[0] == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [4, ' ', ' ', ' ']]
    game.list_board[0] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    game.make_a_move(0)
    assert game.list_board[0] == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', 4]]
    game.list_board[0] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    game.make_a_move(1)
    assert game.list_board[0] == [[2, ' ', ' ', 2], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    game.list_board[0] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    game.make_a_move(2)
    assert game.list_board[0] == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    game.list_board[0] = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', 4, 2]]
    game.make_a_move(1)
    assert game.list_board[0] == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', 2, 4, 2]]

def test_is_over():
    game = init_game("2048")
    game.list_board[0] = generate_board_from_list([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]])
    assert game.is_over() == False
    game.list_board[0] = generate_board_from_list([[2*2**i,4*2**i,8*2**i,16*2**i] for i in range(4)])
    assert game.is_over() == False
