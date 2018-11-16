import src.games.game_2048.board_2048 as board_2048
import src.games.game_2048.player_interaction_2048 as player_interaction_2048
import src.games.game_2048.rules_2048 as rules_2048
import src.games.game_p4.grid_p4 as grid_p4
import src.games.game_p4.player_interaction_p4 as player_interaction_p4
import src.games.game_p4.rules_p4 as rules_p4
from src.board import Board




class Game:
    """
    This is an object which is designed to represent a game using functions written somewhere elem_to_string_size
    The main functions needed to initialize this object are :
        - is_over : returns True if the game is over, and False if it is not
        - make_a_move : modifies the board according to a move given in args but don't return it
        - next_turn : modifies the board according to what is supposed to happen when a player finishes his turn but don't return it (i.e. 2k48 --> spawn a new tile)
        - display_board : returns the string used to display the board
    """
    def __init__(self):
        self.name = "" #name of the game
        self.list_board = [] #list of the boards (one for each players)
        self.score = []
        self.list_player = [] #list of the id of players (0,1,2,...)
        self.move_available = [] #list of the inputs available
        self.board_size = (0,0)
        self.is_over_function = lambda x: None
        self.make_a_move_function = lambda x: None
        self.move_description = "" #what would be displayed to help the player uderstand what input corresponds to which move
        self.map_input_to_move = {} #convert input to move number i.e. {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
        self.map_move_to_input = {} #convert move number to input i.e. {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
        self.is_board_equal = False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        self.theme_number = 0 #theme_number if needed
        self.player_playing = 0 #id of the player which is currently playing
        self.next_turn_function = lambda x: None
        self.calc_score_function = lambda x: None
        self.max_char_size = 2

    def get_board(self, player = 0):
        return self.list_board[player]

    def make_a_move(self, move):
        if self.is_board_equal:
            for i in range(len(self.list_board)):
                self.make_a_move_function(self.list_board[i],move,self.player_playing)
        else:
                self.make_a_move_function(self.list_board[self.player_playing],move,self.player_playing)

    def is_over(self, *args):
        return (self.is_over_function(self.list_board[self.player_playing],*args), self.player_playing)

    def display_board(self, *args):
        return self.list_board[0].grid_to_string_with_size(self.max_char_size)

    def next_turn(self, *args):
        self.next_turn_function(self.list_board[self.player_playing])

    def change_player(self):
        self.player_playing = self.list_player[(self.player_playing +1)%len(self.list_player)]

    def calc_score(self, *args):
        return calc_score_function(self.list_board[self.player_playing],*args)

def init_game(name, vertical_size = 6, horizontal_size = 6, players_number = 2):
    """Create a new game with the name given in args"""
    if name == "2048":
        new_game = Game()
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

    elif name == "p4":
        new_game = Game()
        new_game.name = "p4"
        new_game.score = [0,0]
        new_game.list_board = [Board(vertical_size, horizontal_size) for i in range(2)]
        new_game.list_player = [0,1]
        new_game.board_size = (vertical_size,horizontal_size)
        new_game.move_available = [i for i in range(horizontal_size)] #list of the input available
        new_game.is_over_function = rules_p4.is_over
        new_game.make_a_move_function = rules_p4.make_a_move
        new_game.move_description = player_interaction_p4.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
        new_game.map_input_to_move = {}
        new_game.map_move_to_input = {}
        new_game.is_board_equal = True #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        new_game.next_turn_function = lambda x: x
    else:
        raise Exception("Jeu non reconnu")

    return new_game
