from src.games.games import Game
import src.games.game_2048.grid_2048 as grid_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048


g2k_game = Game()


#Initialisation du jeu

g2k_game.name = "2048"
g2k_game.list_board = [grid_2048.init_grid() for i in range(2)]
g2k_game.list_player = [0,1]
g2k_game.move_available = [0,1,2,3] #list of the input available
g2k_game.is_over_function = rules_2048.is_over
g2k_game.make_a_move_function = rules_2048.make_a_move
g2k_game.move_description = player_interaction_2048.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
g2k_game.display_grid_function = grid_2048.display_grid
g2k_game.map_input_to_move = {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
g2k_game.map_move_to_input = {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
g2k_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
g2k_game.next_turn_function = rules_2048.create_new_tile


def launch():
    while 1:
        print(g2k_game.display_grid(g2k_game.list_board[0]))
        move = player_interaction_2048.get_player_move()
        g2k_game.make_a_move(move)
        if not(g2k_game.is_over()[0]):
            g2k_game.next_turn()
        else:
            print("Vous avez perdu, dommage")
            break

if __name__ == "__main__" :
    launch()
