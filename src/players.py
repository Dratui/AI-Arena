import importlib
from src.games.games import Game

class Player:  #Player class
    def __init__(self,name="default",type_is_ai=False,ai_file_name="human_ai"):
        """
        Initialise the player class, take 3 arguments to be created
        name: the name of the AI (string)
        type_is_ai: boolean to know if the player is an AI  (bool)
        ai_file_name: String of the name of the script of the AI (with the extension (string)
        """
        self.name=name
        self.is_ai=type_is_ai
        self.file=ai_file_name


    def get_move(self,board,game):
        """
        Player function that gives you the move according to the ai that was selected

        """
        package="ai."+self.file
        name="ai_output"
        imported = getattr(__import__(package, fromlist=[name]), name)
        return(imported(board,game))
