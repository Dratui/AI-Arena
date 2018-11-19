import random as rd
#MOVES = ['h','b','g','d']
MOVES= [0,1,2,3]
#Initialisation of a community : number of movements
import src.games.games as games

def calc_score(board):
    sum = 0
    for i in board.get_all_tiles():
        if i!=' ':
            sum += int(int(i))
    return sum

def initialisation(move_numb,pop_size):
    """
    Initialisation of a random population of list of instructions
    
    :param move_numb: number of moves for an individual
    :param pop_size: number of individual in a population
    :return: a population of pop_size individual
    """
    population=[]
    while len(population)<pop_size:
        population.append([rd.choice(MOVES) for i in range(move_numb)])
    return population

def evaluation(population):
    """
    Generate a list of scores to rate each individual compared to each other
    :param population:
    :return: list of scores corresponding for a population
    """
    scores = []
    for individual in population:
        game=games.init_game('2048',calc_score_function = calc_score)
        n=0
        i=0
        while not(game.is_over()[0]) and (n<100):
            if i==len(individual):
                i=0
            game.make_a_move(individual[i])
            game.next_turn()
            i=i+1
            n=n+1
        scores.append(game.calc_score())
    return scores


def selection(population):
    """
    Split the population between the best and the worst.
    :param population:
    :return: the best half of the population.
    """
    ev_pop= evaluation(population)
    pop_score=[]
    for i in range(len(population)):
        pop_score.append([population[i],ev_pop[i]])
    pop_score=sorted(pop_score,key=lambda x: x[1],reverse=True)
    return [x[0] for x in pop_score][len(population) // 2:]

#Mutation with a simple concatenation
def son1(ind1,ind2):
    """ son1 : one half of the first and second half of the second
    2 individual to create one child
    :param ind1:
    :param ind2:
    :return: a new individual
    """
    return ind1[:len(ind1)//2]+ind2[len(ind1)//2:]

#Mutation with a ping pong
def son2(ind1,ind2):
    """ son2: randomly choose between ind1 and ind2
    2 individual to create one child
    :param ind1:
    :param ind2:
    :return: a new individual
    """
    son=[]
    for i in range(len(ind1)):
        if i%2==0:
            son.append(ind1[i])
        else:
            son.append(ind2[i])
    return son

#Mutation random mix
def son3(ind1,ind2):
    """ son2: randomly choose between ind1 and ind2 with a chance ponderation
    2 individual to create one child
    :param ind1:
    :param ind2:
    :return: a new individual
    """
    son=[]
    for i in range(len(ind1)):
        if rd.random()>0.4:
            son.append(ind1[i])
        else:
            son.append(ind2[i])
    return son

def mutation(ind):
    if rd.random()>0.5:
        ind[rd.choice(range(len(ind)))]= rd.choice(MOVES)
    return ind

def new_generation(population):
    pop_size= len(population)
    population=selection(population)
    i=0
    while(len(population) < pop_size):
        if (i==pop_size-2):
            population.append(son2(population[0], population[i + 1]))
            i=0
        else:
            population.append(son2(population[i], population[i + 1]))
            i=i+1
    pop2=[]
    for ind in population:
        pop2.append(mutation(ind))
    return pop2
population=initialisation(2, 50)

for i in range(100):
    print(i)
    population=new_generation(population)
print(population[0:5])
