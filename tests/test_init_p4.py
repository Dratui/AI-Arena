from src.games.game_p4.init_game_p4 import *
from src.games.games import Game
from pytest import *
from src.board import *

def test_create_p4():
    vertical_size, horizontal_size = 6,6
    new_game = Game()
    create_p4(new_game,vertical_size, horizontal_size)
    assert new_game.name == "p4"
    assert new_game.score == [0,0]
    assert [i.get_all_tiles() for i in new_game.list_board] == [Board(vertical_size, horizontal_size).get_all_tiles() for i in range(2)]
    assert new_game.list_player == [0,1]
    assert new_game.board_size == (vertical_size,horizontal_size)
    assert new_game.move_available == [i for i in range(horizontal_size)] #list of the input available
    assert new_game.is_over_function == rules_p4.is_over
    assert new_game.make_a_move_function == rules_p4.make_a_move
    assert new_game.move_description == player_interaction_p4.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
    assert new_game.map_input_to_move == {"1" : 0,'2' : 1,'3' : 2,'4' : 3,'5' : 4,'6' : 5,'7' : 6,'8' : 7,'9' : 8}
    assert new_game.map_move_to_input == {0 : "1",1 : '2',2 : '3',3 : '4',4 : '5',5 : '6',6 : '7',7 : '8',8 : '9'}
    assert new_game.is_board_equal == True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
    assert new_game.move_effective_function == rules_p4.move_effective
    #assert new_game.next_turn_function == lambda x: x
    assert new_game.calc_score_function == score
