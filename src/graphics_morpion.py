from tkinter import *

## Graphical values

NUM2SYM = {' ': ' ', 0:'X', 1:'O'}
TILES_FG_COLOR = {' ':"#ffffff", 0:"#ff0000", 1:"#0009ff"}
TILES_FONT = ("Verdana", 20, "bold")

## Code starts here

# Size of the grid. Should be choosen by the user thanks to another function
grid_size = (3,3)

# Single grid. Should be created by the init function
game_grid = [[' ',1,0] for i in range(10)]

# A button for each case
list_buttons = [[' ' for j in range(grid_size[1])] for i in range(grid_size[0])]

# Window of the game
window = Tk()

# Display function, called at the beginning and then at every change
def display():
    
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            button = Button(window, text = NUM2SYM[game_grid[x][y]], fg = TILES_FG_COLOR[game_grid[x][y]], height = 3, width = 6, command = lambda arg1 = x, arg2 = y : clic(arg1,arg2), font = TILES_FONT)
            button.grid_propagate(0)
            button.grid(column = y, row = x)
            list_buttons[x][y] = button

# Update function
def click(x,y):
    # Should be doing something else
    global game_grid
    
    print(x,y)
    # afficher()
    
    
display()
window.mainloop()



