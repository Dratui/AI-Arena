def score_simple_sum(list_board, current_player):
    """returns the score of a given player (simple score)"""
    sum = 0
    for i in list_board[current_player].get_all_tiles():
        if i!=None:
            sum += int(int(i))
    return sum

def score_eulerian(list_board, current_player):
    """returns the score of a given player (square score)"""
    sum = 0
    for i in list_board[current_player].get_all_tiles():
        if i!=None:
            sum += int(int(i))**2
    return sum
