from tkinter import *
from tkinter import font
from src.tournament import Tournament

TILES_FONT = ("Verdana", 40, "bold")

fenetre=0
canvas=0
Nombre=0
Entree=[]
liste=0
case=0
photo=0

Tournoi=0
listeGames=["2048","Puissance 4","Tic-Tac-Toe (ToDo)","Dames (ToDo)","Echecs (ToDo)","Tetris (ToDo)"]


def name_players():
    global Nombre
    global fenetre
    global Entree
    global Tournoi
    nbrJoueurs=int(Nombre.get())

    Tournoi = Tournament()
    Tournoi.Gtournament_init(nbrJoueurs)

    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('State the name of the AI (simply state h for a human player)')
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

    global Tournoi
    Tournoi.Gselect_players(listeJoueurs)

    global fenetre
    global liste
    global case
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Liste des games')
    liste = Listbox(fenetre)
    global listeGames
    for i,ele in enumerate(listeGames):
        liste.insert(i+1, ele)

    liste.pack()
    global case
    case = IntVar()
    checkbox = Checkbutton(fenetre, text="Display Ai Game",variable=case)
    checkbox.pack()
    bouton = Button(fenetre,text="Valider",command=launch_game)
    bouton.pack()


def launch_game():
    global liste
    global fenetre

    Jeu=liste.get(ACTIVE)
    fenetre.destroy()
    global Tournoi
    Tournoi.Gchoose_game(Jeu)
    fenetre.destroy() #we go out of the mainloop for fenetre here

def init_window():
    global fenetre
    global canvas
    global photo
    if fenetre!=0:
        fenetre.destroy()
    fenetre = Tk()
    fenetre.title("AI Arena")
    canvas = Canvas(fenetre, width=900, height=700, cursor="target")
    photo = PhotoImage(file="graphics/menu.png")

    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.create_text(450,260,text="Play",font=TILES_FONT,fill="#de8421",activefill="#ff3300")
    canvas.pack()
    canvas.bind("<Button-1> ", display_nbrJoueurs)

    canvas.focus_set()
    canvas.pack()


def display_nbrJoueurs(event):
    global Nombre
    global fenetre
    global Tournoi
    Tournoi = Tournament()
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Players')

    label=Label(fenetre,text="Number of players:",bg="yellow").pack(padx=10, pady=10)
    Nombre=Spinbox(fenetre, from_=2, to=10)
    Nombre.pack()
    bouton = Button(fenetre,text="Send",command=name_players)
    bouton.pack()

init_window()
fenetre.mainloop()




print('Launching the game')

display_ai_game=(case.get()==1)

classement=Tournoi.Glaunch_tournament(display_ai_game)

#END Game
#SHOW THE LEADERBOARD
fenetre=Tk()
label = Label(fenetre, text=classement)
label.pack()
bouton = Button(fenetre, text="Menu Principal",command=init_window)
bouton.pack()
fenetre.mainloop()
