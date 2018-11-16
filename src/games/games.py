import game_2048 as g2k
import game_p4 as gp4

class game:
    def __init__(self):
        self.list_board = []
        self.list_player = []
        self.move_available = []

        self.is_over = lambda x: None
        self.make_a_move = lambda x: None

    def get_grid(player = 0):
        return self.list_board[player]

    def is_over( *args):
        return self.is_over( *args)
