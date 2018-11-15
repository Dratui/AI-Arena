from game2048.grid_2048 import *
from pytest import *

from game2048.themes import THEMES

def test_create_grid():
    assert create_grid() == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

def test_init_grid():
    grid = init_grid()
    twoPresent,fourPresent = 0,0

    for i in grid:
        if 2 in i:
            twoPresent = 1 - twoPresent
        if 4 in i:
            fourPresent = 1 - fourPresent
    assert twoPresent and fourPresent

def test_diplay_grid():
    a=""" ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n| 2  |    |    | 2  |\n ==== ==== ==== ==== """
    print(a)
    assert display_grid([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],"0",0)==a

def test_theme_size():
    assert theme_size(THEMES['0']) == 4
    assert theme_size(THEMES['1']) == 2

def test_elem_to_string_size():
    assert elem_to_string_size("test") == 4
    assert elem_to_string_size(4096) == 4
    assert elem_to_string_size(16384) == 5
