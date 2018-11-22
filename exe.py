from tkinter import *
from tkinter import font
from src.tournament import Tournament
from random import randint




#Creation of the fonts used in the interface
Play_font = ("Verdana", 40, "bold")
normal_font=("Verdana", 20)

#Global variables used in the differents functions and steps of the programm
fenetre=0
canvas=0
Nombre=0
Entree=[]
liste=0
case=0
photo=0
Tournoi=0

#Data from the games and AI (only available for them) that are shown in the interface
listeGames=["2048","Puissance 4","Tic-Tac-Toe","Dames (ToDo)","Echecs (ToDo)","Tetris (ToDo)"]
liste_ai=['ai_2048_1','random_ai','bruteforce_ai']

"""
The idea I used for Tkinter is about creating an object fenetre (window)
Each time I want to change the window, I delete it and recreate it from its ashes, like a phoenix
"""

def display_nbrJoueurs(event):
    """
    Function that display the window that allow the user to write the number of players he wants for the tournament
    """
    global Nombre
    global fenetre
    global Tournoi
    Tournoi = Tournament()
    fenetre.destroy()
    fenetre=Tk()
    fenetre.title('Players')



    label=Label(fenetre,text="Number of players:",font=normal_font).pack(padx=10, pady=10)
    Nombre=Spinbox(fenetre, from_=2, to=10,font=normal_font)
    Nombre.pack()
    bouton = Button(fenetre,text="Send",command=name_players,font=normal_font)
    bouton.pack()

def name_players():
    """
    Function that shows the list of players names, that can be changed.
    """
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
    Entree=[]
    for i in range(nbrJoueurs):
        string=liste_ai[randint(0,len(liste_ai)-1)]
        entree=Entry(fenetre,width=20,font=normal_font)
        entree.insert(END,string)
        entree.pack()
        Entree.append(entree)
    bouton = Button(fenetre,text="Valider",command=select_game,font=normal_font)
    bouton.pack()

def select_game():
    """
    Functions that display the game selection menu, and also the option to show the option to display the AI
    """
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
    liste = Listbox(fenetre,font=normal_font)
    global listeGames
    for i,ele in enumerate(listeGames):
        liste.insert(i+1, ele)

    liste.pack()
    case = IntVar()
    checkbox = Checkbutton(fenetre, text="Display Ai Game",variable=case,font=normal_font)
    checkbox.pack()
    bouton = Button(fenetre,text="Valider",command=launch_game,font=normal_font)
    bouton.pack()


def launch_game():
    """
    Function that use the tournament class and launch the tournament, and at the end, shows the leaderboard

    """
    global liste
    global fenetre

    Jeu=liste.get(ACTIVE)
    global case
    display_ai_game=(case.get()==1)
    fenetre.destroy()
    global Tournoi
    Tournoi.Gchoose_game(Jeu)

    print('Launching the game')
    classement=Tournoi.launch_tournament(display_ai_game)

    #END Game
    #SHOW THE LEADERBOARD
    fenetre=Tk()

    label = Label(fenetre, text=classement,font=normal_font)
    label.pack()
    bouton = Button(fenetre, text="Quitter",command=fenetre.destroy,font=normal_font)
    bouton.pack()

def init_window():
    """
    Function to initialise the window object at each beginning (main menu)
    """
    global fenetre
    global canvas
    global photo
    if fenetre==0:
        fenetre = Tk()
    fenetre.title("AI Arena")
    canvas = Canvas(fenetre, width=900, height=700, cursor="target")

    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.create_text(450,260,text="Play",font=Play_font,fill="#de8421",activefill="#ff3300")
    canvas.pack()
    canvas.bind("<Button-1> ", display_nbrJoueurs)

    canvas.focus_set()
    canvas.pack()

#Main loop
fenetre=Tk()
photo = PhotoImage(file="graphics/menu.png")
init_window()
fenetre.mainloop()
