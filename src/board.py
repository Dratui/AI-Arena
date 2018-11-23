import numpy as np
from copy import deepcopy

def get_higher_value(grille):
    """return the maximum value of the grid"""
    max=0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==None: continue
            if grille[i][j]>max:
                max = grille[i][j]
    return max
def generate_board_from_list(grille):
    """return aBoard() object with the grid set to the list given in args"""
    width = len(grille[0])
    height = len(grille)
    tableau=Board(height,width)
    for i in range(height):
        tableau.set_row(i,grille[i])

    return tableau
class Board:
    def __init__(self, height, width):
        self.input=None
        self.height = height
        self.width = width
        self.__grid = [[None for i in range(self.width)] for j in range(self.height)]

    def change_tile(self, row, col,value):
        """
        CHANGE ONE VALUE OF THE GRID
        row: Row (int)
        col: Column (int)
        value: value (str)

        Returns nothing
        """
        self.__grid[row][col]=value


    def read_tile(self, row, col):
        """
        READ ONE VALUE OF THE GRID
        row: Row (int)
        col: Column (int)

        Returns the value (row, col) of the grid
        """
        return self.__grid[row][col]


    def transpose_grid_clockwise(self):
        """
        TRANSPOSE THE BOARD CLOCKWISE
        """
        return [list(elem) for elem in zip(*self.__grid[::-1])]


    def transpose_grid_anticlockwise(self):
        """
        TRANSPOSE THE BOARD ANTICLOCKWISE (CHIBRALLY)
        """
        self.__grid = self.transpose_grid_clockwise()
        self.__grid = self.transpose_grid_clockwise()

        return self.transpose_grid_clockwise()


    def read_row(self, row):
        """
        READ ONE ROW OF THE GRID
        row: Row (int)

        Returns the row as a list
        """
        return self.__grid[row]

    def set_row(self, x,ROW):
        """
        SET ONE ROW OF THE GRID
        row: RowIndex (int)
        ROW; Row (list)

        Returns nothing
        """
        self.__grid[x]=ROW

    def read_column(self, col):
        """
        READ ONE COLUMN OF THE GRID
        col: Column (int)

        Returns the column as a list
        """
        return [self.__grid[i][col] for i in range(self.height)]

    def set_column(self, y,COL):

        """
        SET ONE COL OF THE GRID
        col: ColIndex (int)
        COL; Col (list)

        Returns nothing
        """
        for i in range(self.height):
            self.__grid[i][y]=COL[i]


    def get_all_tiles(self):
        """
        RETURNS A LIST CONTAINING EVERY TILE OF THE GRID
        """
        list_tiles = []
        for i in range(self.height):
            for j in range(self.width):
                list_tiles.append(self.read_tile(i,j))
        return list_tiles

    def get_grid(self):
        return self.__grid


    def grid_to_string_with_size(self, maxsize=8):
        """
        RETURNS A STRING MODELLING THE GRID, TAKING ACCOUNT OF THE BIGGEST VALUE TO AVOID SHIFT
        maxsize : size of the biggest number/value displayed
        """
        width = self.width
        height = self.height
        list_tiles = self.get_all_tiles()
        for i in range(len(list_tiles)):
            if list_tiles[i]==None:
                list_tiles[i]=" "
            else:
                list_tiles[i]=str(list_tiles[i])
        grid_str = """"""
        bord=" "+"="*maxsize
        sticks = bord*width + """\n"""

        lines_str = []
        for i in range(height) :
            line = """|"""
            numbers = [str(list_tiles[width*i+j]).ljust(maxsize) for j in range(width)]
            line = line + "|".join(numbers)
            line = line + """|\n"""
            lines_str.append(line)


        txt=sticks+sticks.join(lines_str)+bord*width+" "
        return txt
