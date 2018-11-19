move_description =""" Entrer le numéro de la colonne ou de le ligne (entre 1 et 3) """


def get_player_move(board):
    """ask and return the move the player want to play"""
    size_horizontal = board.width
    move_x = input("Où voulez-vous jouez ?\n ligne ?")
    move_y = input("\n colonne ?")
    cond = 0
    while 1:
        cond = 0
        if move_x.isdigit() and move_y.isdigit():
            move_x,move_y = int(move_x)-1,int(move_y)-1
            cond = move_x < 3 and move_x >= 0 and move_y < 3 and move_y >= 0
            if cond:
                break
        move_x = input("mouvement invalide ?\n ligne ?")
        move_y = input("\n colonne ?")
    return move_x*3 + move_y
