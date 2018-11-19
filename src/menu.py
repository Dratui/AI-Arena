from tkinter import *
from tkinter import font

TILES_FONT = ("Verdana", 40, "bold")

fenetre = Tk()
fenetre.title("AI Arena")
canvas = Canvas(fenetre, width=900, height=700, cursor="target")
photo = PhotoImage(file="../graphics/menu.PNG")



def afficher():
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()


def clavier(event):
    touche = event.keysym
    for i in range(4):
        for j in range(4):
            game_grid[i][j]="0"
    afficher()

    fenetre.update()

afficher()
canvas.focus_set()
canvas.pack()

fenetre.mainloop()
