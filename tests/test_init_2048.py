from src.games.game_2048.init_game_2048 import *
from src.games.games import Game
from pytest import *
from src.board import *

def test_create_2048():
    new_game = Game()
    create_2048(new_game)
    players_number = 2
    assert new_game.name == "2048"
    assert new_game.score == [0 for i in range(players_number)]
    assert new_game.list_player == [i for i in range(players_number)]
    assert new_game.board_size == (4,4)
    assert new_game.move_available == [0,1,2,3] #list of the input available
    assert new_game.is_over_function == rules_2048.is_over
    assert new_game.make_a_move_function == rules_2048.make_a_move
    assert new_game.move_description == player_interaction_2048.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
    assert new_game.map_input_to_move == {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
    assert new_game.map_move_to_input == {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
    assert new_game.is_board_equal == False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
    assert new_game.next_turn_function == rules_2048.create_new_tile
    assert new_game.calc_score_function == rules_2048.calc_score
    assert new_game.move_effective_function == rules_2048.move_effective
