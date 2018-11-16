from src.games.game_p4.rules_p4 import *
from pytest import *


def test_is_last_move_winning():
    assert is_last_move_winning([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, ' ', ' ', 1]],0,0) == False
    assert is_last_move_winning([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, 0, 0, 0]],0,0) == True
    assert is_last_move_winning([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, 0, 0, 0]],1,0) == False
    assert is_last_move_winning([[0, ' ', ' ', ' '], [0, ' ', ' ', ' '], [0, ' ', ' ', ' '], [0, ' ', ' ', 1]],0,0) == True

def test_make_a_move():
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [0, ' ', ' ', 1]], 1, 0) ==[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [1, ' ', ' ', ' '], [0, ' ', ' ', 1]]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [1, ' ', 0, 0]],0,2) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', 0, ' '], [1,' ',0,0]]
