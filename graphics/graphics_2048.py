# Graphical interface for a 2048 game.



from tkinter import *
from src.board import Board
from src.games.games import Game
from src.board import generate_board_from_list

## Graphical values

TILES_BG_COLOR = {None: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {None: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = ("Verdana", 20, "bold")

## Code starts here

def initialization():
    # Creates the window
    window = Tk()
    return window

test_game=Game()
board1=generate_board_from_list([[2],[None]])
board0=generate_board_from_list([[2],[None]])
test_game.list_board=[board0,board1]

def main(window,game):
    board0=game.list_board[0]
    board1=game.list_board[1]


    # Update function
    def keyboard(event):
        global list_grids
        key = event.keysym

        ## Updates for the player at the left
        if key == "z":
            # Update "high", chosen randomly here
            board0.input = "h"

        elif key == "s":
            # Update "down", chosen randomly here
            board0.input = "b"

        elif key == "q":
            # Update "left", chosen randomly here
            board0.input = "g"

        elif key == "d":
            # Update "right", chosen randomly here
            board0.input = "d"

        ## Updates for the player at the right
        if key == "Up":
            # Update "high", chosen randomly here
            board1.input = "h"

        elif key == "Down":
            # Update "down", chosen randomly here
            board1.input = "b"

        elif key == "Left":
            # Update "left", chosen randomly here
            board1.input = "g"

        elif key == "Right":
            # Update "right", chosen randomly here
            board1.input ="d"

    ## Handling the keyboard input
    window.bind("<Key>", keyboard)

    ## Window's loop
    window.mainloop()





















def update_display(window, game=test_game):
# Size of the grid. Should be choosen by the user thanks to another function
    grid_size = (Board0.height,Board0.width)
    
    # A grid for each player. Should be created by the init function
    game_grid0 = Board0.get_grid()
    game_grid1 = Board1.get_grid()
    list_grids = [game_grid0, game_grid1]
    
    # A canva for each player
    canvas0 = Canvas(window,bg="#FFCC99", height=400, width=400)
    canvas1 = Canvas(window,bg="#FFCC99", height=400, width=400)
    list_canvas = [canvas0,canvas1]
    
    
    # Display function, called at the beginning and then at every change
    def display():
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

        display()
        window.update()
        
    ## First display
    display()
    
    ## Handling the keyboard input
    window.bind("<Key>", clavier_0)
    
    ## Window's loop
    window.mainloop()

    

            
    
            
