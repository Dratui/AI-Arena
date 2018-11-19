import src.games.game_morpion.player_interaction_morpion as player_interaction_morpion
import src.games.game_morpion.rules_morpion as rules_morpion
from src.board import Board


def create_morpion(new_game):
        new_game.name = "morpion"
        new_game.score = [0,0]
        new_game.list_board = [Board(3,3) for i in range(2)]
        new_game.list_player = [0,1]
        new_game.board_size = (3,3)
        move_available = []
        for i in range(3):
            for j in range(3):
                move_available.append((i,j))
        new_game.move_available = move_available#list of the input available
        new_game.is_over_function = rules_morpion.is_over
        new_game.make_a_move_function = rules_morpion.make_a_move
        new_game.move_description = player_interaction_morpion.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {}
        new_game.map_move_to_input = {}
        new_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        new_game.next_turn_function = lambda x: x
