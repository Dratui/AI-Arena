import numpy as np

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
        """
        TRANSPOSE THE BOARD CLOCKWISE
        """
        return [list(elem) for elem in zip(*self.grid[::-1])]
        
        
    def transpose_grid_anticlockwise(self):
        """
        TRANSPOSE THE BOARD ANTICLOCKWISE (CHIBRALLY)
        """
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
    
    
    def get_all_tiles(self):
        """
        RETURNS A LIST CONTAINING EVERY TILE OF THE GRID
        """
        list_tiles = []
        for i,j in range(self.height):
            for j in range(self.width):
                list_tiles.append(self.read_tile(i,j))
        return list_tiles
    
        
    def grid_to_string_with_size(self, maxsize):
        """
        RETURNS A STRING MODELLING THE GRID, TAKING ACCOUNT OF THE BIGGEST VALUE TO AVOID SHIFT
        maxsize : size of the biggest number/value displayed 
        """
        width = self.width
        height = self.height
        list_tiles = self.get_all_tiles
        grid_str = """"""
        sticks = """ ==="""*width + """ \n"""
        string_grid = sticks
        lines_str = []
        for i in range(height) :
            line = """|"""
            numbers = [str(list_tiles[width*i+j]).ljust(n) for j in range(width)]
            line = line + "|".join(numbers)
            line = line + """|\n"""
            lines_str.append(line)
        grid_str = sticks.join(lines_str)
        grid_str = sticks + grid_str + """ ==="""*width + """ """
        return grid_str
        
    
    
    

    