import src.games.games as Games
import AI.random_ai as AI
from src.board import *
from pytest import *

def test_ai_output():
    game = Games.init_game("2048")
    assert AI.ai_output([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]], game) in [0,1,2,3]
    game = Games.init_game("p4")
    assert AI.ai_output([[None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [2, None, None, 2, None, None]], game) in [0,1,2,3,4,5]
    game = Games.init_game("ttt")
    assert AI.ai_output([[None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [2, None, None, 2, None, None]], game) in range(36)
    game.list_board[0]= generate_board_from_list([[0, 0, 0], [None, 0, 0], [0, 0, 0]])
    assert AI.ai_output([[0, 0, 0], [None, 0, 0], [0, 0, 0]], game) == 3
