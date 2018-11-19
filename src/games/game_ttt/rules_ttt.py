def make_a_move(board,move,player):
    if board.read_tile(move//3, move %3) == " ":
        board.change_tile(move//3, move %3 ,player)

def move_effective(board):
    list = []
    for i in range(3):
        for j in range(3):
            if board.read_tile(i,j) == " ":
                list.append(3*i+j)
    return list

def is_over(board):
    for player in range(2):
        for move_x in range(3):
            for move_y in range(3):
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
    return False
