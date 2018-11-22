import ai.ai_2048_1 as AI
from pytest import *
import src.games.games as Games

def test_ai_output():
    game = Games.init_game("2048")
    assert AI.ai_output([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]], game) in [0,1,2,3]

