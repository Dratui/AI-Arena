from src.games.game_2048.player_interaction_2048 import *
from pytest import *

def test_player_theme(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert player_setup_theme() == 0

def test_get_player_move(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "d")
    assert get_player_move() == 0
    monkeypatch.setattr('builtins.input', lambda x: "h")
    assert get_player_move() == 2

def test_player_setup_size(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "4")
    assert player_setup_size() == 4
    monkeypatch.setattr('builtins.input', lambda x: "2")
    assert player_setup_size() == 2
