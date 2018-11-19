import random as rd
#MOVES = ['h','b','g','d']
MOVES= [0,1,2,3]
#Initialisation of a community : number of movements
import src.games.games as games



def initialisation(move_numb,pop_size): #Initialisation of a random population of list of instructions
    population=[]
    while len(population)<pop_size:
        population.append([rd.choice(MOVES) for i in range(move_numb)])
    return population

def evaluation(population): #Generate a list of scores to rate each individual compared to each other
    scores = []
    for individual in population:
        game=games.init_game('2048')
        i=0
        while not(game.is_over()):
            if i==len(individual):
                i=0
            game.make_a_move(individual[i]) #Pas généré si le moove est pas possible
            i=i+1
        scores.append(game.calc_score())
    return scores

def selection(population): #
    pop_score = list(set(zip(population, evaluation(population))))
    sorted(pop_score,key=lambda x: x[1])
    return (list(set([x[0] for x in pop_score])))[population // 2:]

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
def new_generation(population):
    pop_size= len(population)
    population=selection(population)
    i=0
    while(len(population) < pop_size):
        if (i==pop_size-2):
            population.append(son1(population[0], population[i + 1]))
            i=0
        else:
            population.append(son1(population[i], population[i + 1]))
            i=i+1
    pop2=[]
    for ind in population:
        pop2.append(mutation(ind))
    return pop2
population=initialisation(2, 4)
print(population)
print(evaluation(population))

