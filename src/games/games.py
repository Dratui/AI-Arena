import src.games.game_2048 as g2k
import src.games.game_p4 as gp4

class Game:
    def __init__(self):
        self.name = ""
        self.list_board = []
        self.list_player = []
        self.move_available = [] #list of the input available
        self.is_over_function = lambda x: None
        self.make_a_move_function = lambda x: None
        self.move_description = "" #what would be displayed to help the player uderstand what input corresponds to which move
        self.display_grid_function = lambda x: None
        self.map_input_to_move = {}
        self.map_move_to_input = {}
        self.is_board_equal = False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
        self.theme_number = 0
        self.player_playing = 0
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
