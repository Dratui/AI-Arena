



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for i in range(self.width)] for j in range(self.height)]
    
    def change(self, x,y,value):
        """
        CHANGE ONE VALUE OF THE GRID
        x: Lignes (int)
        y: Colonnes (int)
        value: valeur (str)
        
        Returns nothing
        """
        self.grid[x][y]=value

    def transpose(self):
        return [list(elem) for elem in zip(*A[::-1])]
    
    
    