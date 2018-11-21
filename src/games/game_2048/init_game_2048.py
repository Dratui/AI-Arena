import src.games.game_2048.board_2048 as board_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048
from src.board import Board



def create_2048(new_game, players_number =2):
        new_game.name = "2048"
        new_game.score = [0 for i in range(players_number)]
        new_game.list_board = [board_2048.init_board(Board(4,4)) for i in range(players_number)]
        new_game.list_player = [i for i in range(players_number)]
        new_game.board_size = (4,4)
        new_game.move_available = [0,1,2,3] #list of the input available
        new_game.is_over_function = rules_2048.is_over
        new_game.make_a_move_function = rules_2048.make_a_move
        new_game.move_description = player_interaction_2048.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
        new_game.map_move_to_input = {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
        new_game.is_board_equal = False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        new_game.next_turn_function = rules_2048.create_new_tile
        new_game.calc_score_function = rules_2048.calc_score
        new_game.move_effective_function = rules_2048.move_effective
