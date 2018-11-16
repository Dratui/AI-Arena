class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[' ' for i in range(self.width)] for j in range(self.height)]

        
    def change_tile(self, row, col,value):
        """
        CHANGE ONE VALUE OF THE GRID
        row: Row (int)
        col: Column (int)
        value: value (str)
        
        Returns nothing
        """
        self.grid[row][col]=value
        
    def read_tile(self, row, col):
        """
        READ ONE VALUE OF THE GRID
        row: Row (int)
        col: Column (int)
        
        Returns the value (row, col) of the grid
        """
        return self.grid[row][col]

    def transpose_grid_clockwise(self):
        return [list(elem) for elem in zip(*self.grid[::-1])]
        
    def transpose_grid_anticlockwise(self):
        self.transpose_grid_clockwise()
        self.transpose_grid_clockwise()
        return self.transpose_grid_clockwise()
        
    def read_row(self, x):
        """
        READ ONE ROW OF THE GRID
        row: Row (int)
        
        Returns the row as a list
        """
        return self.grid[row]
        
    def read_column(self, col):
        """
        READ ONE COLUMN OF THE GRID
        col: Column (int)
        
        Returns the column as a list
        """
        return [self.grid[i][col] for i in range(self.height)]


    
    