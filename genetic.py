import random as rd
#MOVES = ['h','b','g','d']
MOVES= [0,1,2,3]
#Initialisation of a community : number of movements
import src.games.games as games



def initialisation(move_numb,pop_size):
    pop=[]
    while len(pop)<pop_size:
        pop.append([rd.choices(MOVES) for i in range(pop_size)])
    return pop

def evaluation(pop):
    scores = []
    for indiviual in pop:
        game=games.init_game('2048')
        i=0
        while(not(game.is_over())):
            if i==len(indiviual):
                i=0
            game.make_a_move(indiviual[i]) #Pas généré si le moove est pas possible
            i=i+1
        scores.append(sum([sum(row) for row in game.display_grid()]))
    return scores

def selection(pop):
    pop_score = list(set(zip(pop,evaluation(pop))))
    sorted(pop_score,key=lambda x: x[1])
    return
