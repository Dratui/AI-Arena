
from tkinter import *
from src.board import Board
from src.games.games import Game
from src.board import generate_board_from_list

# a test game class in order to be able to test the graphical functions

test_game=Game()
board1=generate_board_from_list([[2],[None]])
board0=generate_board_from_list([[2],[None]])
test_game.list_board=[board0,board1]

# the function you need to call to update the graphical display
def update_display(window, game=test_game):

    #the two boards
    Board0=game.list_board[0]
    Board1=game.list_board[1]
    #we add the window attribute to be able to update the window elsewhere
    game.window=window
    grid_size = (Board0.height,Board0.width)

    #the keyboard function that triggers when a key is pressed
    def keyboard(event):
        key = event.keysym
        if key == "z":
            Board0.input = "h"
        elif key == "s":
            Board0.input = "b"

        elif key == "q":
            Board0.input = "g"

        elif key == "d":
            Board0.input = "d"

        elif key == "Up":
            Board1.input = "h"

        elif key == "Down":
            Board1.input = "b"

        elif key == "Left":
            Board1.input = "g"

        elif key == "Right":
            Board1.input ="d"

    game_grid0 = Board0.get_grid()
    game_grid1 = Board1.get_grid()

    list_grids = [game_grid0, game_grid1]


    if game.name=="2048":
        #the tiles are colored
        TILES_BG_COLOR = {None: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                          16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                          128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                          1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                          8192: "#24ba63"}

        TILES_FG_COLOR = {None: "#9e948a", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                          16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                          256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                          2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

        TILES_FONT = ("Verdana", 20, "bold")

        # A canva for each player

        canvas0 = Canvas(window,bg="#FFCC99", height=400, width=400)
        canvas1 = Canvas(window,bg="#FFCC99", height=400, width=400)
        canvas0.focus_set()

        list_canvas = [canvas0,canvas1]

        #only modifies the canvas of the player that is playing
        if not game.is_over()[0]:

            i=game.player_playing
            for x in range(grid_size[0]):
                for y in range(grid_size[1]):
                    case = LabelFrame(list_canvas[i], bg = TILES_BG_COLOR[list_grids[i][x][y]], height = 100, width = 100)
                    case.grid_propagate(0)
                    case.grid(column = y, row = x)
                    text = Label(case, text = str(list_grids[i][x][y]), bg = TILES_BG_COLOR[list_grids[i][x][y]], fg = TILES_FG_COLOR[list_grids[i][x][y]] , font = TILES_FONT)
                    text.place(x=50, y=50, anchor="center")
            list_canvas[i].grid_propagate(0)
            list_canvas[i].grid(column = i, row = 0)

        window.update()
        window.bind("<Key>",keyboard)


    if game.name=='ttt':
        NUM2SYM = {None: ' ', 0:'X', 1:'O'}
        TILES_FG_COLOR = {None:"#ffffff", 0:"#ff0000", 1:"#0009ff"}
        TILES_FONT = ("Verdana", 20, "bold")

        list_buttons = [[None for j in range(grid_size[1])] for i in range(grid_size[0])]


        def click(x,y):
            Board0.input = str(x+1) + "," + str(y+1)
            Board1.input = str(x+1) + "," + str(y+1)

        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                button = Button(window, text = NUM2SYM[game_grid0[x][y]], fg = TILES_FG_COLOR[game_grid0[x][y]], height = 3, width = 6, command = lambda arg1 = x, arg2 = y : click(arg1,arg2), font = TILES_FONT)
                button.grid_propagate(0)
                button.grid(column = y, row = x)
                list_buttons[x][y] = button

        window.update()

    if game.name=='p4':
        TILES_FG_COLOR = {None:"#ffffff", 0:"#ff0000", 1:"#ffff00"}

        TILES_FONT = ("Verdana", 20, "bold")

        # Lists of canvas and buttons
        list_canvas = [[None for j in range(grid_size[1])] for i in range(grid_size[0])]
        list_buttons = [None for j in range(grid_size[1])]

        # Update function
        def click(i):
            Board0.input = str(i+1)
            Board1.input = str(i+1)

        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                case = Canvas(window, bg = "#ffffff", height = 50, width = 50)
                case.grid_propagate(0)
                case.grid(column = y, row = x)
                text = Label(case, text = 'O', fg = TILES_FG_COLOR[game_grid0[x][y]], bg = "#ffffff", font = TILES_FONT)
                text.place(x=25, y=25, anchor="center")

        for y in range(grid_size[1]) :
            button = Button(window, text = "Ici", height = 3, width = 6, command = lambda arg = y : click(arg))
            button.grid_propagate(0)
            button.grid(column = y, row = 0)
            list_buttons[y] = button

        window.update()
