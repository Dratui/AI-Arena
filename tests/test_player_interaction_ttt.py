from src.games.game_ttt.player_interaction_ttt import *
from pytest import *
from src.games.games import *

a= 1
def f(x):
    global a
    a+=1
    return str(a)

b= 3
def g(x):
    global b
    print(b)
    b+=1
    return str(b)

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_get_player_move(monkeypatch):
    new_game = init_game("ttt")
    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(["2","1"]))
    assert get_player_move(new_game.list_board[0]) == 1
    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(["3","2"]))
    assert get_player_move(new_game.list_board[0]) == 5
