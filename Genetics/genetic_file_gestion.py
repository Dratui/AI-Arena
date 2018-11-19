from .genetic import genetic_algorithm
POP_NUMB=["population_number","pop_number","pop_numb"]
MOVES_NUMB=["moves_numb","individual_size","individuals_size","ind_size","move_number","moves_number"]
GENE_NUMB=['generation_number',"gen_number","gene_numb","gene_number","generation_size","gene_size","gen_size"]
FILE_NAME={'filename','file_name',"namefile","name_file",'file'}
SCORE_FUNCTION={"score_function",'scorefunction','score'}

def do_work_for_genetic(worktodo):
    source_file = open("."+worktodo,'r')

    for line in source_file:
        parameters=line.split(' ') #parameters must be : genetic_algorithm population_number moves_number generation_number
        i=1
        dict_parameters={}
        while i<len(parameters):
            if(parameters[i] in  POP_NUMB):
                dict_parameters[POP_NUMB[0]]=parameters[i+1]
                i=i+1
            elif(parameters[i] in MOVES_NUMB):
                dict_parameters[MOVES_NUMB[0]]=parameters[i+1]
                i=i+1
            elif(parameters[i] in GENE_NUMB):
                dict_parameters[GENE_NUMB[0]]=parameters[i+1]
                i=i+1
            elif(parameters[i] in FILE_NAME):
                dict_parameters[FILE_NAME[0]]=parameters[i+1]
                i=i+1
            elif(parameters[i] in SCORE_FUNCTION):
                dict_parameters[SCORE_FUNCTION[0]]=parameters[i+1]
                i=i+1
            i=i+1
        results_file = open(dict_parameters[SCORE_FUNCTION[0]] ,'a')
        results_file.write("Results of {} for {} = {} and {} = {} and {} = {} and {} = {} are {}".format(parameters[0],MOVES_NUMB[0],dict_parameters[MOVES_NUMB[0]],POP_NUMB[0],dict_parameters[POP_NUMB[0]],GENE_NUMB[0],dict_parameters[GENE_NUMB[0]],dict_parameters[POP_NUMB[0]],dict_parameters[GENE_NUMB[0]],dict_parameters[SCORE_FUNCTION[0]]))


def calc_score_sum(board):
    """
    Simple sum of all the tiles
    :param board:
    :return:
    """
    sum = 0
    for i in board.get_all_tiles():
        if i!=' ':
            sum += int(int(i))
    return sum
