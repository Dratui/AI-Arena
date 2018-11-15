



class board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for i in range(self.width)] for j in range(self.height)]
        
    