from src.games.game_2048.rules_2048 import *
from pytest import *

from src.games.game_2048.themes import THEMES

def test_evolve_line():
    assert evolve_line([" " for i in range(4)]) == [" " for i in range(4)]
    assert evolve_line([" ",4,4,8]) == [8,8," "," "]
    assert evolve_line([2, ' ', ' ', 2]) == [4,' ',' ',' ']
    assert evolve_line([2, 4, ' ', 2]) == [2,4,2,' ']

def test_make_a_move():
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],1) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [4, ' ', ' ', ' ']]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],0) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', 4]]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],2) == [[2, ' ', ' ', 2], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],3) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]
    assert make_a_move([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', 4, 2]],0) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', 2, 4, 2]]

def test_is_over():
    assert is_over([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]]) == False
    assert is_over([[2*2**i,4*2**i,8*2**i,16*2**i] for i in range(4)]) == True
