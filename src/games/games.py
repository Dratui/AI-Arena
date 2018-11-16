import src.games.game_2048 as g2k
import src.games.game_p4 as gp4

class Game:
    def __init__(self):
        self.list_board = []
        self.list_player = []
        self.move_available = [] #list of the input available
        self.is_over_function = lambda x: None
        self.make_a_move_function = lambda x: None
        self.move_description = "" #what would be displayed to help the player uderstand what input corresponds to which move
        self.display_grid_function = lambda x: None
        self.map_input_to_move = {}

    def get_grid(self, player = 0):
        return self.list_board[player]

    def make_a_move(self, move,player):
        self.grid = self.make_a_move_function(self.grid, move,player)

    def is_over(self, *args):
        return self.is_over_function(*args)

    def display_grid(self, *args):
        return self.display_grid_function(*args)
