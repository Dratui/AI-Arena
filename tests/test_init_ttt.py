from src.games.game_ttt.init_game_ttt import *
from src.games.games import Game
from pytest import *
from src.board import *
def test_create_ttt():
        new_game = Game()
        create_ttt(new_game)
        assert new_game.name == "ttt"
        assert new_game.score == [0,0]
        assert [i.get_all_tiles() for i in new_game.list_board] == [Board(3,3).get_all_tiles() for i in range(2)]
        assert new_game.list_player == [0,1]
        assert new_game.board_size == (3,3)
        assert new_game.move_available == [i for i in range(9)]
        assert new_game.is_over_function == rules_ttt.is_over
        assert new_game.make_a_move_function == rules_ttt.make_a_move
        assert new_game.move_description == player_interaction_ttt.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        assert new_game.map_input_to_move == {"1,1" : 0,'1,2' : 1,'1,3' : 2,'2,1' : 3,'2,2' : 4,'2,3' : 5,'3,1' : 6,'3,2' : 7,'3,3' : 8}
        assert new_game.map_move_to_input == {0 : "1,1",1 : '1,2',2 : '1,3',3 : '2,1',4 : '2,2',5 : '2,3',6 : '3,1',7 : '3,2',8 : '3,3'}
        assert new_game.is_board_equal == True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        #assert new_game.next_turn_function == lambda x: x
        assert new_game.move_effective_function == rules_ttt.move_effective
        assert new_game.calc_score_function == rules_ttt.calc_score
