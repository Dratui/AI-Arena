def calc_score(list_board, current_player):
    sum = 0
    for i in list_board[current_player].get_all_tiles():
        if i!=' ':
            sum += int(int(i))
    return sum
