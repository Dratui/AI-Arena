from tkinter import *

##

TILES_FG_COLOR = {' ':"#ffffff", 0:"#ff0000", 1:"#ffff00"}

TILES_FONT = ("Verdana", 20, "bold")

##

grid_size = (10,10)

game_grid = [[' ',1,0,1,0,1,' ',0,0,' '] for i in range(10)]
# list_canvas = [[' ' for j in range(10)] for i in range(10)]
list_buttons = [' ' for j in range(grid_size[1])]

fenetre = Tk()


def afficher():
    
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            case = Canvas(fenetre, bg = "#ffffff", height = 50, width = 50)
            case.grid_propagate(0)
            case.grid(column = y, row = x)
            text = Label(case, text = 'O', fg = TILES_FG_COLOR[game_grid[x][y]], bg = "#ffffff", font = TILES_FONT)
            text.place(x=25, y=25, anchor="center")
    for y in range(grid_size[1]) :
        button = Button(fenetre, text = "Ici", height = 3, width = 6, command = lambda arg = y : clic(arg))
        button.grid_propagate(0)
        button.grid(column = y, row = 0)
        list_buttons[y] = button
        

def clic(i):
    
    print("blabla")
    global game_grid
    
    if i == 0 :
        game_grid = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] for i in range(10)]
    
    elif i == 1 :
        game_grid = [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
        
    elif i == 2 :    
        game_grid = [[1,1,1,1,1,1,1,1,1,1] for i in range(10)]
        
    print(game_grid)
    afficher()
    fenetre.update()

afficher()
fenetre.mainloop()
