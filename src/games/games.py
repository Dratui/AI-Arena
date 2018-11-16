class Game:
    def __init__(self):
        self.move_available = [0,1,2,3] #list of the input available
        self.move_description = "Veuillez aller en haut(h), à droite (d), en bas (b) ou à gauche(g)"
        self.map_move_to_input = {0:"h",1:"d",2:"b",3:"g"}
