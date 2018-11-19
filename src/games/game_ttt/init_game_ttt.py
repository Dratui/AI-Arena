import src.games.game_ttt.player_interaction_ttt as player_interaction_ttt
import src.games.game_ttt.rules_ttt as rules_ttt
from src.board import Board


def create_ttt(new_game):
        new_game.name = "ttt"
        new_game.score = [0,0]
        new_game.list_board = [Board(3,3) for i in range(2)]
        new_game.list_player = [0,1]
        new_game.board_size = (3,3)
        move_available = []
        for i in range(3):
            for j in range(3):
                move_available.append((i,j))
        new_game.move_available = move_available#list of the input available
<<<<<<< HEAD:src/games/game_ttt/init_game_ttt.py
        new_game.is_over_function = rules_ttt.is_over
        new_game.make_a_move_function = rules_ttt.make_a_move
        new_game.move_description = player_interaction_ttt.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {}
        new_game.map_move_to_input = {}
=======
        new_game.is_over_function = rules_morpion.is_over
        new_game.make_a_move_function = rules_morpion.make_a_move
        new_game.move_description = player_interaction_morpion.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {"1,1" : 0,'1,2' : 1,'1,3' : 2,'2,1' : 3,'2,2' : 4,'2,3' : 5,'3,1' : 1,'3,2' : 2,'3,3' : 8}
        new_game.map_move_to_input = {0 : "1,1",1 : '1,2',2 : '1,3',3 : '2,1',4 : '2,2',5 : '2,3',6 : '3,1',7 : '3,2',8 : '3,3'}
>>>>>>> 264fd5f4c6f456854c828e4045c7fd412656a59c:src/games/game_morpion/init_game_morpion.py
        new_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        new_game.next_turn_function = lambda x: x
        new_game.move_effective_function = rules_ttt.move_effective
