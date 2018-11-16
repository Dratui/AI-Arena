from IA.ia_file_name import ia_output
from src.games.games import Game

class Player:  #
    def __init__(self,name="default",type_is_ia=False,ia_file_name="human_ia"):
        self.name=name
        self.is_ia=type_is_ia
        self.file=ia_file_name

    def get_move(self,board,game):
        return(ia_output(board,game))


game_test=Game()
board="lol"
test_player=Player(name="joueur_1")
print(test_player.get_move(board,game_test))
