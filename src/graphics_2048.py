from tkinter import *

## Valeurs graphiques

TILES_BG_COLOR = {'0': "#9e948a", '2': "#eee4da", '4': "#ede0c8", '8': "#f1b078", \
                  '16': "#eb8c52", '32': "#f67c5f", '64': "#f65e3b", \
                  '128': "#edcf72", '256': "#edcc61", '512': "#edc850", \
                  '1024': "#edc53f", '2048': "#edc22e", '4096': "#5eda92", \
                  '8192': "#24ba63"}

TILES_FG_COLOR = {'0': "#776e65", '2': "#776e65", '4': "#776e65", '8': "#f9f6f2", \
                  '16': "#f9f6f2", '32': "#f9f6f2", '64': "#f9f6f2", '128': "#f9f6f2", \
                  '256': "#f9f6f2", '512': "#f9f6f2", '1024': "#f9f6f2", \
                  '2048': "#f9f6f2", '4096': "#f9f6f2", '8192': "#f9f6f2"}

TILES_FONT = ("Verdana", 20, "bold")

## 


grid_size = (4,4)

game_grid1 = [['0','2','4','8'],['16','32','64','128'],['256','512','1024','2048'],['4096','8192','0','2']]
game_grid2 = [['0','2','4','8'],['16','32','64','128'],['256','512','1024','2048'],['4096','8192','0','2']]
list_grids = [game_grid1, game_grid2]
fenetre = Tk()
canvas1 = Canvas(fenetre,bg="#FFCC99", height=400, width=400)
canvas2 = Canvas(fenetre,bg="#FFCC99", height=400, width=400)
list_canvas = [canvas1,canvas2]



def afficher():
    for i in range(len(list_canvas)):
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                case = LabelFrame(list_canvas[i], bg = TILES_BG_COLOR[list_grids[i][x][y]], height = 100, width = 100)
                case.grid_propagate(0)
                case.grid(column = y, row = x)
                text = Label(case, text = str(list_grids[i][x][y]), bg = TILES_BG_COLOR[list_grids[i][x][y]], fg = TILES_FG_COLOR[list_grids[i][x][y]] , font = TILES_FONT)
                text.place(x=50, y=50, anchor="center")
        list_canvas[i].grid_propagate(0)
        list_canvas[i].grid(column = i, row = 0)
            
def clavier_0(event):
    global list_grids
    touche = event.keysym
    
    if touche == "z":
        # On fait là MàJ Haut, ici random
        for i in range(4):
            for j in range(4):
                list_grids[0][i][j]="0"
                
    elif touche == "s":
        # On fait là MàJ Bas, ici random
        for i in range(4):
            for j in range(4):
                list_grids[0][i][j]="2"
                
    elif touche == "q":
        # On fait là MàJ Gauche, ici random
        for i in range(4):
            for j in range(4):
                list_grids[0][i][j]="4"
    
    elif touche == "d":
        # On fait là MàJ Droite, ici random
        for i in range(4):
            for j in range(4):
                list_grids[0][i][j]="8"
    
    if touche == "Up":
        # On fait là MàJ Haut, ici random
        for i in range(4):
            for j in range(4):
                list_grids[1][i][j]="0"
                
    elif touche == "Down":
        # On fait là MàJ Bas, ici random
        for i in range(4):
            for j in range(4):
                list_grids[1][i][j]="2"
                
    elif touche == "Left":
        # On fait là MàJ Gauche, ici random
        for i in range(4):
            for j in range(4):
                list_grids[1][i][j]="4"
    
    elif touche == "Right":
        # On fait là MàJ Droite, ici random
        for i in range(4):
            for j in range(4):
                list_grids[1][i][j]="8"
    
        
    afficher()
    fenetre.update()
    

afficher()
fenetre.bind("<Key>", clavier_0)
fenetre.mainloop()

    

            
    
            