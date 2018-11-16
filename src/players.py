import importlib
from src.games.games import Game

class Player:  #Player class
    def __init__(self,name="default",type_is_ia=False,ia_file_name="human_ia"):
        self.name=name
        self.is_ia=type_is_ia
        self.file=ia_file_name


    def get_move(self,board,game): # Player function that gives you the move according to the ia that was selected
        package="IA."+self.file
        name="ia_output"
        imported = getattr(__import__(package, fromlist=[name]), name)
        return(imported(board,game))


