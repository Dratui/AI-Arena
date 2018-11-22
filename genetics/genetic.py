import random as rd
#from genetics.score_functions import calc_score
GAME = '2048'
MOVES= [0,1,2,3]
#Initialisation of a community : number of movements
import src.games.games as games


#Way to attribute a score to algorithms

def calc_score_sum_squared(board):
    """
    Somme tous les tiles au carré
    Sum of all the tiles by squared
    :param board:
    :return:
    """
    sum = 0
    for i in board.get_all_tiles():
        if i!=None:
            sum += int(int(i))
    return sum

#Initialisation
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

#Evaluation
def evaluation(population,calc_score):
    """
    Generate a list of scores to rate each individual compared to each other
    :param population:
    :return: list of scores corresponding for a population
    """
    scores = []
    for individual in population:
        game=games.init_game(name=GAME)
        game.calc_score_function=calc_score
        i=0

        while not(game.is_over()[0] or len([x for x in individual if x in game.get_move_effective()])):
            #The game ends if the game is over or of all moves in the individual won't do anything to the board
            if i==len(individual):
                i=0
            game.make_a_move(individual[i])
            game.next_turn()
            i=i+1
        scores.append(game.calc_score())
    return scores

#Selection of the best individuals
def selection(population,calc_score):
    """
    Split the population between the best and the worst.
    :param population:
    :return: the best half of the population.
    """
    ev_pop= evaluation(population,calc_score)
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
    :return: a mutated individual (or not, who knows)
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
    """ son2: randomly choose between ind1 and ind2 with a chance ponderated
    2 individual to create one child
    :param ind1:
    :param ind2:
    :return: a mutated individual (or not, who knows)
    """
    son=[]
    for i in range(len(ind1)):
        if rd.random()>0.4:
            son.append(ind1[i])
        else:
            son.append(ind2[i])
    return son

#Mutation of individuals
def mutation(ind):
    """
    Mutate randomly an individual
    :param ind:
    :return: a mutated individual (or not, who knows)
    """
    if rd.random() > 0.5:
        ind[rd.choice(range(len(ind)))]= rd.choice(MOVES)
    return ind

#Creation of a new generation with
def new_generation(population,calc_score):
    """
    Creates a new generation population.
    :param population:
    :return: a new population : the next generation
    """
    pop_size= len(population)
    population=selection(population,calc_score)
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

def results(population):
    """
    At the end, we check the number of each sequence that is the same and list them by descendant values.
    :param population:
    :return: sequences with number of individual with this
    """
    sequences=[]
    numb_ind_per_sequence=[]
    for ind in population:
        if ind in sequences:
            i=sequences.index(ind)
            numb_ind_per_sequence[i]=numb_ind_per_sequence[i]+1
        else:
            sequences.append(ind)
            numb_ind_per_sequence.append(1)
    return sorted([(sequences[i],numb_ind_per_sequence[i]) for i in range(len(sequences))],key=lambda x:x[1],reverse=True)
            #Return the descendant list of (individual, number of presence)

def genetic_algorithm(individual_size, population_size, number_of_generation,calc_score):
    """
    Final algorithme which print the result of the wanted algorithm
    :param population_size:
    :param individual_size:
    :param number_of_generation:
    :return: results
    """
    population=initialisation(individual_size,population_size)
    for i in range(number_of_generation):
        if(i*100)%number_of_generation==0:
            print("Genetic algorithm of {} individuals of {} size with {} iterations at {} %".format(population_size,individual_size,number_of_generation,(i*100)//number_of_generation ))
        population=new_generation(population,calc_score)
    return results(population)

#print(genetic_algorithm(2,10,100,calc_score))
