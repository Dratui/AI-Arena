from gamep4.player_interaction_p4 import *
from pytest import *

a= 4
def f(x):
    global a
    a+=1
    print(a)
    return str(a)

def test_get_player_move(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "2")
    assert get_player_move(8,[[' ' for i in range(8)] for k in range(5)]) == 1
    monkeypatch.setattr('builtins.input', lambda x: "4")
    assert get_player_move(8,[[' ' for i in range(8)] for k in range(5)]) == 3

def test_player_setup_size(monkeypatch):
    monkeypatch.setattr('builtins.input', f)
    assert player_setup_size() == (5,6,7)
