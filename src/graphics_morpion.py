from tkinter import *

##

NUM2SYM = {' ': ' ', 0:'X', 1:'O'}
TILES_FG_COLOR = {' ':"#ffffff", 0:"#ff0000", 1:"#0009ff"}
TILES_FONT = ("Verdana", 20, "bold")



##

grid_size = (3,3)

game_grid = [[' ',1,0] for i in range(10)]
list_buttons = [[' ' for j in range(grid_size[1])] for i in range(grid_size[0])]

fenetre = Tk()

def afficher():
    
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            print(NUM2SYM[game_grid[x][y]])
            button = Button(fenetre, text = NUM2SYM[game_grid[x][y]], fg = TILES_FG_COLOR[game_grid[x][y]], height = 3, width = 6, command = lambda arg1 = x, arg2 = y : clic(arg1,arg2), font = TILES_FONT)
            button.grid_propagate(0)
            button.grid(column = y, row = x)
            list_buttons[x][y] = button
            
def clic(x,y) :
    print("okay")
    global game_grid
    
    print(x,y)
    # afficher()
    
    
afficher()
fenetre.mainloop()



