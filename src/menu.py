from tkinter import *
from tkinter import font

TILES_FONT = ("Verdana", 40, "bold")

fenetre = Tk()
canvas = Canvas(fenetre, bg="#FFCC99", width=900, height=900,cursor="target")
photo = PhotoImage(file="../menu.png")



def afficher():
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()

    Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=LEFT, padx=30, pady=30)

    # frame 2
    Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Frame2.pack(side=LEFT, padx=10, pady=10)

    #Creation du frame qui sera a l'interieur
    Button(Frame1, text ='Launch the Game',font=TILES_FONT,cursor="target")
    Button(Frame2, text ='Leave',font=TILES_FONT,cursor="target")

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
