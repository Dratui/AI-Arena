from tkinter import *
from tkinter import font

TILES_FONT = ("Verdana", 40, "bold")

fenetre = Tk()
fenetre.title("AI Arena")
canvas = Canvas(fenetre, width=900, height=700, cursor="target")
photo = PhotoImage(file="../graphics/menu.PNG")
Nombre=0
Entree=[]
liste=0

listeGames=["2048","Puissance 4","Tic-Tac-Toe (ToDo)","Dames (ToDo)","Echecs (ToDo)","Tetris (ToDo)"]


def play(event):
    global Nombre
    global fenetre
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Joueurs')
   
    label=Label(fenetre,text="Nombre de joueurs:",bg="yellow").pack(padx=10, pady=10)
    Nombre=Spinbox(fenetre, from_=2, to=10)
    Nombre.pack()
    bouton = Button(fenetre,text="Valider",command=name_players)
    bouton.pack()

def name_players():
    global Nombre
    global fenetre
    global Entree
    
    nbrJoueurs=int(Nombre.get())
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Name of the players')
    for i in range(nbrJoueurs):
        string="Joueurs "+str(i+1)
        entree=Entry(fenetre,textvariable=string,width=20)
        entree.insert(END,string)
        entree.pack()
        Entree.append(entree)
    bouton = Button(fenetre,text="Valider",command=select_game)
    bouton.pack()
    
def select_game():
    listeJoueurs=[]
    for i in range(len(Entree)):
        name=Entree[i].get()
        listeJoueurs.append(name)
    
    global fenetre
    global liste
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Liste des games')
    liste = Listbox(fenetre)
    global listeGames
    for i,ele in enumerate(listeGames):
        liste.insert(i+1, ele)
    
    liste.pack()  
    bouton = Button(fenetre,text="Valider",command=launch_game)
    bouton.pack()
def launch_game():
    global liste
    Jeu=liste.get(ACTIVE)
    print('Launching the game')
    print(Jeu)

    
    
    
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.create_text(450,260,text="Play",font=TILES_FONT,fill="#de8421",activefill="#ff3300")
canvas.pack()
canvas.bind("<Button-1> ", play)



canvas.focus_set()
canvas.pack()

fenetre.mainloop()
