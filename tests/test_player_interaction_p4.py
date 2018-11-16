from src.games.game_p4.player_interaction_p4 import *
from pytest import *
from src.games.games import *

a= 4
def f(x):
    global a
    a+=1
    print(a)
    return str(a)

def test_get_player_move(monkeypatch):
    new_game = init_game("p4")
    monkeypatch.setattr('builtins.input', lambda x: "2")
    assert get_player_move(new_game.list_board[0]) == 1
    monkeypatch.setattr('builtins.input', lambda x: "4")
    assert get_player_move(new_game.list_board[0]) == 3

def test_player_setup_size(monkeypatch):
    monkeypatch.setattr('builtins.input', f)
    assert player_setup_size() == (5,6,7)
