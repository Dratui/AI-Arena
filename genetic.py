import random as rd
#MOVES = ['h','b','g','d']
MOVES= [0,1,2,3]
#Initialisation of a community : number of movements
import src.games.games as games



def initialisation(move_numb,pop_size):
    pop=[]
    while len(pop)<pop_size:
        pop.append([rd.choice(MOVES) for i in range(move_numb)])
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
        scores.append(game.calc_score())
    return scores

def selection(pop):
    pop_score = list(set(zip(pop,evaluation(pop))))
    sorted(pop_score,key=lambda x: x[1])
    return (list(set([x[0] for x in pop_score])))[pop//2:]

#Mutation with a simple concatenation
def son1(ind1,ind2):
    return ind1[:len(ind1)//2]+ind2[len(ind1)//2:]
#Mutation with a ping pong
def son2(ind1,ind2):
    son=[]
    for i in range(len(ind1)):
        if i%2==0:
            son.append(ind1)
        else:
            son.append(ind2)
    return son
#Mutation random mix

def son3(ind1,ind2):
    son=[]
    for i in range(len(ind1)):
        if rd.random()>0.4:
            son.append(ind1)
        else:
            son.append(ind2)
    return son
def mutation(ind):
    if rd.random>0.5:
        ind[rd.choice(range(len(ind)))]= rd.choice(MOVES)
    return ind
def new_generation(pop):
    pop_size= len(pop)
    pop=selection(pop)
    i=0
    while(len(pop)<pop_size):
        if (i==pop_size-2):
            pop.append(son1(pop[0],pop[i+1]))
            i=0
        else:
            pop.append(son1(pop[i],pop[i+1]))
            i=i+1
    pop2=[]
    for ind in pop:
        pop2.append(mutation(ind))
    return pop2
pop=initialisation(2,4)
print(pop)
print(selection(pop))

