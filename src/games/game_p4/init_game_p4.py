import src.games.game_p4.player_interaction_p4 as player_interaction_p4
import src.games.game_p4.rules_p4 as rules_p4

from src.board import Board



def create_p4(new_game, vertical_size, horizontal_size):
    """Set the attributes of the Game() object for p4"""
        new_game.name = "p4"
        new_game.score = [0,0]
        new_game.list_board = [Board(vertical_size, horizontal_size) for i in range(2)]
        new_game.list_player = [0,1]
        new_game.board_size = (vertical_size,horizontal_size)
        new_game.move_available = [i for i in range(horizontal_size)] #list of the input available
        new_game.is_over_function = rules_p4.is_over
        new_game.make_a_move_function = rules_p4.make_a_move
        new_game.move_description = player_interaction_p4.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {"1" : 0,'2' : 1,'3' : 2,'4' : 3,'5' : 4,'6' : 5,'7' : 6,'8' : 7,'9' : 8}
        new_game.map_move_to_input = {0 : "1",1 : '2',2 : '3',3 : '4',4 : '5',5 : '6',6 : '7',7 : '8',8 : '9'}
        new_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        new_game.move_effective_function = rules_p4.move_effective
        new_game.next_turn_function = lambda x: x
        new_game.calc_score_function = rules_p4.calc_score
