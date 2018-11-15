from gamep4.grid_p4 import *
from pytest import *


def test_create_grid():
    assert create_grid(5,5) == [[' 'for i in range(5)]for k in range(5)]
    assert create_grid(8,5) == [[' 'for i in range(8)]for k in range(5)]

def test_display_grid():
    assert display_grid([[' 'for i in range(4)]for k in range(4)], 4) == "| 1  | 2  | 3  | 4  |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== "
