from tkinter import *

##

TILES_FG_COLOR = {' ':"#ffffff", 0:"#ff0000", 1:"#ff8000"}

##

grid_size = (10,10)

game_grid = [[' ',1,0,1,0,1,' ',0,0,' '] for i in range(10)]
list_canvas = [[' ' for j in range(10)] for i in range(10)]

fenetre = Tk()


def afficher():
    
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            case = Canvas(fenetre, bg = "#ffffff", height = 50, width = 50)
            case.grid_propagate(0)
            case.grid(column = y, row = x)
            text = Label(case, text = 'O', fg = TILES_FG_COLOR[game_grid[x][y]])
            text.place(x=25, y=25, anchor="center")

afficher()
# fenetre.bind("<Key>", clavier_0)
fenetre.mainloop()
