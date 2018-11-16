from src.games.games import Game, init_game
import src.games.game_2048.grid_2048 as grid_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048


"""g2k_game = init_game("2048")


def launch():
    while 1:
        print(g2k_game.list_board[0].grid_to_string_with_size(3))
        move = player_interaction_2048.get_player_move()
        g2k_game.make_a_move(move)
        if not(g2k_game.is_over()[0]):
            g2k_game.next_turn()
        else:
            print("Vous avez perdu, dommage")
            break

if __name__ == "__main__" :
    launch()"""


gp4_game = init_game("p4")


def launch():
    while 1:
        print(gp4_game.list_board[0].grid_to_string_with_size(3))
        move = player_interaction_p4.get_player_move(gp4_game.list_board[0])
        gp4_game.make_a_move(move)
        if not(gp4_game.is_over(gp4_game.list_board[0],move, gp4_game.player_playing)[0]):
            gp4.next_turn()
        else:
            print("Vous avez perdu, dommage")
            break

if __name__ == "__main__" :
    launch()
