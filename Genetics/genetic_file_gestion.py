from Genetics.genetic import genetic_algorithm
POP_NUMB=["population_number","pop_number","pop_numb"]
MOVES_NUMB=["moves_numb","individual_size","individuals_size","ind_size","move_number","moves_number"]
GENE_NUMB=['generation_number',"gen_number","gene_numb","gene_number","generation_size","gene_size","gen_size"]
FILE_NAME=['filename','file_name',"namefile","name_file",'file']
SCORE_FUNCTION=["score_function",'scorefunction','score']

def do_work_for_genetic(worktodo):
    """
    Execution to a text file
    :param worktodo: a texte file with commands to execute
    :return:
    """
    source_file = open(worktodo,'r')
    lines_source_file=[]
    for line in source_file:
        if not(line in ['\n',' \n',None,'','\n ']):
            lines_source_file.append(line)

    for line in lines_source_file:
        parameters=line.replace('\n','').split(None) #parameters must be : genetic_algorithm population_number moves_number generation_number score_function=
        i=1
        dict_parameters={}
        while i<len(parameters):
            #print(dict_parameters)
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
        print(dict_parameters)
        print(dict_parameters[FILE_NAME[0]])
        results_file = open(dict_parameters[FILE_NAME[0]]+'.txt' ,'a+')
        import Genetics.score_functions
        score_function=getattr(Genetics.score_functions,dict_parameters[SCORE_FUNCTION[0]])
        results_file.write("Results of {} for {} = {} and {} = {} and {} = {} with {} = {} are {}. \n \n".format(parameters[0],MOVES_NUMB[0],dict_parameters[MOVES_NUMB[0]],POP_NUMB[0],dict_parameters[POP_NUMB[0]],GENE_NUMB[0],dict_parameters[GENE_NUMB[0]],SCORE_FUNCTION[0],dict_parameters[SCORE_FUNCTION[0]],genetic_algorithm(int(dict_parameters[MOVES_NUMB[0]]),int(dict_parameters[POP_NUMB[0]]),int(dict_parameters[GENE_NUMB[0]]),score_function)))

#do_work_for_genetic('to_do_simple_sum.txt')
