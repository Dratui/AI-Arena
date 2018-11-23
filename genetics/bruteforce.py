#Not_smart_algorithm
from genetics.genetic import evaluation,selection
from copy import deepcopy
from src.games.game_2048.rules_2048 import calc_score
DEPTH = 5
def ia_output(game,depth=DEPTH):
    game=deepcopy(game)
    possibilities =  generate_all_move(game)
    scores=evaluation(possibilities,calc_score)
    next_move=selection(possibilities,scores)[0][0]
    return next_move

def generate_all_move(game,depth):
    possibilites = [[]]
    new_possibilities=[]
    for depth in range(depth):
        for move in game.move_available():
            for poss in possibilites:
                new_possibilities.append(poss.append(move))
        possibilites=new_possibilities
        new_possibilities=[]
    return possibilites

#dddldkl
