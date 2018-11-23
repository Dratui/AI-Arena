from tkinter import *
from board import Board

## Graphical values

NUM2SYM = {None: ' ', 0:'X', 1:'O'}
TILES_FG_COLOR = {None:"#ffffff", 0:"#ff0000", 1:"#0009ff"}
TILES_FONT = ("Verdana", 20, "bold")

## Code starts here


    
def initialization():
    # Creates the window
    window = Tk()
    return window
    
    
def update_display(Board, window):
    # Size of the grid.
    grid_size = (Board.height, Board.width)
    
    # Grid created by reading the board.
    game_grid = Board.get_grid()
    
    # A button for each case
    list_buttons = [[None for j in range(grid_size[1])] for i in range(grid_size[0])]
    
    # Display function, called at the beginning and then at every change
    def display():
        
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                button = Button(window, text = NUM2SYM[game_grid[x][y]], fg = TILES_FG_COLOR[game_grid[x][y]], height = 3, width = 6, command = lambda arg1 = x, arg2 = y : click(arg1,arg2), font = TILES_FONT)
                button.grid_propagate(0)
                button.grid(column = y, row = x)
                list_buttons[x][y] = button
    
    # Update function
    def click(x,y):
        Board.input = str(x+1) + "," + str(y+1)
        
        
    display()
    window.mainloop()

    
def close_window(window):
    # Closes the window
    window.destroy
    
    




