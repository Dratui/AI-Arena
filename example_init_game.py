from src.games.games import Game, init_game
import src.games.game_p4.player_interaction_p4 as player_interaction_p4
import src.games.game_p4.rules_p4 as rules_p4
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048
import src.games.game_ttt.player_interaction_ttt as player_interaction_ttt
import src.games.game_ttt.rules_ttt as rules_ttt


g2k_game = init_game("2048")
gp4_game = init_game("p4")
ttt_game = init_game("ttt")

game = "p4"

def launch():
    if game == "2048":
        while 1:
            print(g2k_game.list_board[0].grid_to_string_with_size(8))
            move = player_interaction_2048.get_player_move()
            while not(move in g2k_game.get_move_effective()):
                print("mouvement inutile")
                move = player_interaction_2048.get_player_move()
            g2k_game.make_a_move(move)
            if not(g2k_game.is_over()[0]):
                g2k_game.next_turn()
            else:
                print("Vous avez perdu, dommage")
                break
    if game == "p4":
        while 1:
            print("joueur", gp4_game.player_playing)
            print(gp4_game.list_board[0].grid_to_string_with_size(3))
            move = player_interaction_p4.get_player_move(gp4_game.list_board[0])
            gp4_game.make_a_move(move)
            if not(gp4_game.is_over()[0]):
                gp4_game.next_turn()
                gp4_game.change_player()
            else:
                print("Le joueur ",  gp4_game.player_playing, "gagne")
                break
    if game == "ttt":
        while 1:
            print("joueur", ttt_game.player_playing)
            print(ttt_game.list_board[0].grid_to_string_with_size(3))
            move = player_interaction_ttt.get_player_move(ttt_game.list_board[0])
            while not(move in ttt_game.get_move_effective()):
                print("mouvement inutile")
                move = player_interaction_ttt.get_player_move(ttt_game.list_board[0])
            ttt_game.make_a_move(move)
            if not(ttt_game.is_over()[0]):
                ttt_game.next_turn()
                ttt_game.change_player()
            else:
                print("Le joueur ",  ttt_game.player_playing, "gagne")
                break

if __name__ == "__main__" :
    launch()
