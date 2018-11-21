import AI.2048_AI_1 as AI
from pytest import *

def test_ai_output():
    assert ai_output([[None, None, None, None], [None, None, None, None], [None, None, None, None], [2, None, None, 2]], "2048") in [0,1,2,3]