def make_a_move(board,  move, player):
    """update the grid to acknowledge the last move"""
    i= 0
    while board.read_tile(i,move) == None:
        if i < board.width-1:
            i+=1
        else:
            i+=1
            break
    board.change_tile(i-1,move, player)

def is_over(board):
    """check if the last move played makes the player who played it win,
    and return in the second argument the number of the winning player"""

    for move in range(board.width):
        if board.read_tile(board.height-1 ,move) != None:
            for player in range(2):
                i= 0
                while board.read_tile(i,move) == None:
                    i+=1
                list_near_points = [] #list of the number of the player payns in each direction starting from the last one beginning with up then going clockwise
                directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
                for dir in directions:
                    k=0
                    while i+dir[0]*k >= 0 and i+dir[0]*k < board.width and move+k*dir[1] >= 0 and move+k*dir[1] <board.width:
                        if board.read_tile(i+dir[0]*k,move+k*dir[1]) == player:
                            k+=1
                        else:
                            break
                    list_near_points.append(k-1)
                for k in range(4):
                    if list_near_points[k]+list_near_points[k+4] >2 :
                        return True
    is_full = True
    for move in range(board.width):
        for i in range(board.height):
            if board.read_tile(i,move) == None:
                is_full = False
    if is_full:
        return True
    return False

def move_effective(board):
    list = []
    for i in range(board.width):
        if board.read_tile(0,i) == None:
            list.append(i)
    return list

def calc_score(list_board, player_playing):
    """Returns a score of 1 for the player that has won"""
    if is_over(list_board[0]) :
        return 1
    else :
        return 0
