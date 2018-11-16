import src.games.games
import src.games.game_2048 as g2k

g2k_game = Game()


#Initialisation du jeu

g2k_game.name = "2048"
g2k_game.list_board = [g2k.grid_2048.init_grid() for i in range(2)]
g2k_game.list_player = [0,1]
g2k_game.move_available = [0,1,2,3] #list of the input available
g2k_game.is_over_function = g2k.rules_2048.is_over
g2k_game.make_a_move_function = g2k.rules_2048.make_a_move
g2k_game.move_description = g2k.player_interaction_2048.move_description #what would be displayed to help the player uderstand what input corresponds to which move
g2k_game.display_grid_function = g2k.grid_2048
g2k_game.map_input_to_move = {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
g2k_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
