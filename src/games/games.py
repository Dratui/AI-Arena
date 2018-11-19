import src.games.game_2048.board_2048 as board_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048
import src.games.game_2048.init_game_2048 as init_game_2048

import src.games.game_p4.player_interaction_p4 as player_interaction_p4
import src.games.game_p4.rules_p4 as rules_p4
import src.games.game_p4.init_game_p4 as init_game_p4

import src.games.game_ttt.player_interaction_ttt as player_interaction_ttt
import src.games.game_ttt.rules_ttt as rules_ttt
import src.games.game_ttt.init_game_ttt as init_game_ttt

from src.board import Board




class Game:
    """
    This is an object which is designed to represent a game using functions written somewhere elem_to_string_size
    The main functions needed to initialize this object are :
        - is_over : returns a tuple, with the first item being True if the game is over, and False if it is not and the second being the player that win
        - make_a_move : modifies the board according to a move given in args but don't return it
        - next_turn : modifies the board according to what is supposed to happen when a player finishes his turn but don't return it (i.e. 2k48 --> spawn a new tile)
        - move_effective : returns the list of the move that will have an efect on the game (i.e. not the move that will do nothing)
        - display_board : returns the string used to display the board
    """
    def __init__(self, name = "", number_player = 2, move_available = [], board_size = (4,4), make_a_move_function = lambda x: None, is_over_function = lambda x: None,  next_turn_function = lambda x: None,
                move_effective_function = lambda x: None, calc_score_function = lambda x: None, move_description = "", map_input_to_move = {}, map_move_to_input = {}, is_board_equal = False , theme_number = 0,
                player_playing = 0, max_char_size = 2):

        self.name = name#name of the game
        self.list_board = [Board(board_size[0], board_size[1]) for i in range(number_player)] #list of the boards (one for each players)
        self.score = [0 for i in range(number_player)]
        self.list_player = [i for i in range(number_player)] #list of the id of players (0,1,2,...)
        self.move_available = move_available #list of the inputs available
        self.board_size = board_size
        self.is_over_function = is_over_function
        self.make_a_move_function = make_a_move_function
        self.move_description = move_description #what would be displayed to help the player uderstand what input corresponds to which move
        self.map_input_to_move = map_input_to_move #convert input to move number i.e. {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
        self.map_move_to_input = map_move_to_input #convert move number to input i.e. {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
        self.is_board_equal = is_board_equal #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        self.theme_number = theme_number #theme_number if needed
        self.player_playing = player_playing #id of the player which is currently playing
        self.next_turn_function = next_turn_function
        self.calc_score_function = calc_score_function
        self.max_char_size = max_char_size
        self.move_effective_function = move_effective_function

    def get_board(self, player = 0):
        return self.list_board[player]

    def make_a_move(self, move):
        if self.is_board_equal:
            for i in range(len(self.list_board)):
                self.make_a_move_function(self.list_board[i],move,self.player_playing)
        else:
                self.make_a_move_function(self.list_board[self.player_playing],move,self.player_playing)

    def is_over(self, *args, player = None):
        if player == None:
            player = self.player_playing
        return (self.is_over_function(self.list_board[player],*args), player)

    def all_over(self, *args):
        test = True
        for i in range(len(self.list_board)):
            test = test and self.is_over_function(self.list_board[i])
        return test

    def display_board(self, board_number = None, *args):
        if board_number == None:
            board_number = self.player_playing
        return self.list_board[board_number].grid_to_string_with_size(self.max_char_size)

    def next_turn(self, *args):
        self.next_turn_function(self.list_board[self.player_playing])

    def change_player(self):
        self.player_playing = self.list_player[(self.player_playing +1)%len(self.list_player)]

    def calc_score(self, *args):
        return self.calc_score_function(self.list_board, self.player_playing,*args)

    def get_move_effective(self):
        return self.move_effective_function(self.list_board[self.player_playing])

def init_game(name, vertical_size = 6, horizontal_size = 6, players_number = 2):
    """Create a new game with the name given in args"""
    if name == "2048":
        new_game = Game()
        init_game_2048.create_2048(new_game,players_number)
        return new_game

    elif name == "p4":
        new_game = Game()
        init_game_p4.create_p4(new_game, vertical_size, horizontal_size)
        return new_game
    elif name == "ttt":
        new_game = Game()
        init_game_ttt.create_ttt(new_game)
        return new_game
    else:
        raise Exception("Jeu non reconnu")
