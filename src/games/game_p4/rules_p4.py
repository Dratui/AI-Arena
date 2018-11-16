def make_a_move(grid, player, move):
    """update the grid to acknowledge the last move"""
    i= 0
    while grid[i][move] == " ":
        if i < len(grid)-1:
            i+=1
        else:
            i+=1
            break
    grid[i-1][move] = player
    return grid

def is_over(grid,player,move):
    """check if the last move played makes the player who played it win, and return in the second argument the number of the winning player"""
    i= 0
    while grid[i][move] == " ":
        i+=1
    list_near_points = [] #list of the number of the player payns in each direction starting from the last one beginning with up then going clockwise
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    for dir in directions:
        k=0
        while i+dir[0]*k >= 0 and i+dir[0]*k < len(grid) and move+k*dir[1] >= 0 and move+k*dir[1] < len(grid[0]):
            if grid[i+dir[0]*k][move+k*dir[1]] == player:
                k+=1
            else:
                break
        list_near_points.append(k-1)
    for k in range(4):
        if list_near_points[k]+list_near_points[k+4] >2 :
            return (True, player)
    return (False, player)
