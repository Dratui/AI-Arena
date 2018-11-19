from tkinter import *
from tkinter import font

TILES_FONT = ("Verdana", 40, "bold")

fenetre = Tk()
fenetre.title("AI Arena")
canvas = Canvas(fenetre, width=900, height=700, cursor="target")
photo = PhotoImage(file="../graphics/menu.PNG")

canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.create_text(450,260,text="Play",font=TILES_FONT,fill="#de8421",activefill="#ff3300") 
canvas.pack()
def clic_play(events):
    print("Play")
def clavier(event):
    touche = event.keysym
    for i in range(4):
        for j in range(4):
            game_grid[i][j]="0"
    

    fenetre.update()

canvas.focus_set()
canvas.pack()

fenetre.mainloop()
