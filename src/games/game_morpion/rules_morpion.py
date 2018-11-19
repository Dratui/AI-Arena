def make_a_move(board,move,player):
    if board.read_tile(move[0],move[1]) == " ":
        board.change_tile(move[0],move[1],player)

def move_effective(board):
    list = []
    for i in range(3):
        for j in range(3):
            if board.read_tile(i,j) == " ":
                list.append((i,j))
    return list

def is_over(board, move, player):
    i= 0
    while board.read_tile(i,move) == " ":
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
        if list_near_points[k]+list_near_points[k+4] >1 :
            return True
    return False
