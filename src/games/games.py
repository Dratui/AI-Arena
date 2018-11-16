import src.games.game_2048 as g2k
import src.games.game_p4 as gp4




class Game:
    """
    This is an object which is designed to represent a game using functions written somewhere elem_to_string_size
    The main functions needed to initialize this object are :
        - is_over : which returns True if the game is over, and False if it is not
        - make_a_move : which modifies the grid according to a move given in args
        - next_turn : which modifies the grid according to what is supposed to happen when a player finishes his turn (i.e. 2k48 --> spawn a new tile)
        - display_grid : which return the string used to display the board
    """
    def __init__(self):
        self.name = "" #name of the game
        self.list_board = [] #list of the boards (one for each players)
        self.list_player = [] #list of the id of players (0,1,2,...)
        self.move_available = [] #list of the inputs available
        self.is_over_function = lambda x: None
        self.make_a_move_function = lambda x: None
        self.move_description = "" #what would be displayed to help the player uderstand what input corresponds to which move
        self.display_grid_function = lambda x: None
        self.map_input_to_move = {} #convert input to move number i.e. {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
        self.map_move_to_input = {} #convert move number to input i.e. {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
        self.is_board_equal = False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        self.theme_number = 0 #theme_number if needed
        self.player_playing = 0 #id of the player which is currently playing
        self.next_turn_function = lambda x: None

    def get_grid(self, player = 0):
        return self.list_board[player]

    def make_a_move(self, move):
        if self.is_board_equal:
            new_grid = self.make_a_move_function(self.list_board[self.player_playing], move, self.player_playing)
            for i in range(len(self.list_board)):
                self.list_board[i] = new_grid
        else:
            self.list_board[self.player_playing] = self.make_a_move_function(self.list_board[self.player_playing], move, self.player_playing)

    def is_over(self, *args):
        return (self.is_over_function(self.list_board[self.player_playing],*args), self.player_playing)

    def display_grid(self, *args):
        return self.display_grid_function(*args)

    def next_turn(self, *args):
        self.list_board[self.player_playing] = self.next_turn_function(self.list_board[self.player_playing])

    def change_player(self):
        self.player_playing = self.list_player[(self.player_playing +1)%len(self.list_player)]
