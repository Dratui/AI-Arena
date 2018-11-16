from src.games.games import Game, init_game
import src.games.game_2048.grid_2048 as grid_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048


g2k_game = init_game("2048")


def launch():
    while 1:
        print(g2k_game.list_board[0].grid_to_string_with_size(6))
        move = player_interaction_2048.get_player_move()
        g2k_game.make_a_move(move)
        if not(g2k_game.is_over()[0]):
            g2k_game.next_turn()
        else:
            print("Vous avez perdu, dommage")
            break

if __name__ == "__main__" :
    launch()
