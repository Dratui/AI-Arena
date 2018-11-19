from tkinter import *
from tkinter import font



fenetre = Tk()
canvas = Canvas(fenetre,bg="#FFCC99", width=900, height=900)

def afficher():
    #Creation du frame qui sera a l'interieur
    L=LabelFrame(canvas,text="Jeu de tournoi", padx=20,pady=20)
    L.pack(fill='both',expand="yes")

    Label(L,text="Tout ce qu'on a à l'intérieur de la frame").pack

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
