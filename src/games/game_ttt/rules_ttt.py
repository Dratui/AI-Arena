def make_a_move(board,move,player):
    """Updates and returns the board after making the move asked in args"""
    if board.read_tile(move//board.width, move %board.width) == None:
        board.change_tile(move//board.width, move %board.width ,player)
    return board

def move_effective(board):
    """Returns the list of the move that would have an effect on the game"""
    list = []
    for i in range(board.height):
        for j in range(board.width):
            if board.read_tile(i,j) == None:
                list.append(3*i+j)
    return list

def is_over(board):
    """Returns True if the game is over, False if not"""
    for player in range(2):
        for move_x in range(board.height):
            for move_y in range(board.width):
                list_near_points = [] #list of the number of the player payns in each direction starting from the last one beginning with up then going clockwise
                directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
                for dir in directions:
                    k=0
                    while move_y+dir[0]*k >= 0 and move_y+dir[0]*k < board.width and move_x+k*dir[1] >= 0 and move_x+k*dir[1] <board.width:
                        if board.read_tile(move_y+dir[0]*k,move_x+k*dir[1]) == player:
                            k+=1
                        else:
                            break
                    list_near_points.append(k-1)
                for k in range(4):
                    if list_near_points[k]+list_near_points[k+4] >1 :
                        return True
    is_full = True
    for move in range(board.width):
        for i in range(board.height):
            if board.read_tile(i,move) == None:
                is_full = False
    if is_full:
        return True
    return False

def calc_score(list_board, player):
    """Resturns the score of a given player"""
    board = list_board[player]
    for move_x in range(list_board[player].height):
        for move_y in range(list_board[player].width):
            list_near_points = [] #list of the number of the player payns in each direction starting from the last one beginning with up then going clockwise
            directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
            for dir in directions:
                k=0
                while move_y+dir[0]*k >= 0 and move_y+dir[0]*k < board.width and move_x+k*dir[1] >= 0 and move_x+k*dir[1] <board.width:
                    if board.read_tile(move_y+dir[0]*k,move_x+k*dir[1]) == player:
                        k+=1
                    else:
                        break
                list_near_points.append(k-1)
            for k in range(4):
                if list_near_points[k]+list_near_points[k+4] >1 :
                    return 1
    return 0
