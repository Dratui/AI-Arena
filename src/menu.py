from tkinter import *
from tkinter import font

TILES_FONT = ("Verdana", 40, "bold")

fenetre = Tk()
fenetre.title("AI Arena")
canvas = Canvas(fenetre, width=900, height=700, cursor="target")
photo = PhotoImage(file="../graphics/menu.PNG")

def clic(events):
    
    print("Play")

def Joueurs(event):
    
    fenetrejoueurs=Tk()
    fenetrejoueurs.title('Joueurs')
   
    label=Label(fenetrejoueurs,text="Nombre de joueurs:",bg="yellow").pack(padx=10, pady=10)
    Nombre=Spinbox(fenetrejoueurs, from_=0, to=10)
    Nombre.pack()
    
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.create_text(450,260,text="Play",font=TILES_FONT,fill="#de8421",activefill="#ff3300")
canvas.pack()
canvas.bind("<Button-1> ", Joueurs)



canvas.focus_set()
canvas.pack()

fenetre.mainloop()
