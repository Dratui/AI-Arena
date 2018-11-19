from tkinter import *
from tkinter import font


##

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}


##

grid_size = (4,4)

game_grid = [[0,2,4,8],[16,32,64,128],[256,512,1024,2048],[4096,8192,0,2]]
graphical_grid = []

fenetre = Tk()
background = Frame(fenetre,bg="#FFCC99", height=900, width=900)


for x in range(grid_size[0]) :
    for y in range(grid_size[1]) :
        case = LabelFrame(fenetre, bg = TILES_BG_COLOR[game_grid[x][y]], height = 100, width = 100)
        case.grid_propagate(0)
        case.grid(column = y, row = x)
        text = Label(case, text = str(game_grid[x][y]), bg = TILES_BG_COLOR[game_grid[x][y]], fg = TILES_FG_COLOR[game_grid[x][y]] , font = ("Verdana", 20, "bold"))
        text.place(x=50, y=50, anchor="center")
              

fenetre.mainloop()




