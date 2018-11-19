move_description =""" Entrer le numéro de la colonne """


def player_setup_size():
    """ask and return the size of the grid wanted by the player"""
    size_number_horizontal = input("Rentrez la taille horizontale de la grille que vous souhaitez avoir")
    while size_number_horizontal.isdigit() == False:
        size_number_horizontal = input("Entrée invalide, réessayer s'il vous plaît")
    size_number_vertical = input("Rentrez la taille verticale de la grille que vous souhaitez avoir")
    while size_number_vertical.isdigit() == False:
        size_number_vertical = input("Entrée invalide, réessayer s'il vous plaît")
    size_column = input("Rentrez la taille des colonnes de la grille que vous souhaitez avoir")
    while size_column.isdigit() == False:
        size_column = input("Entrée invalide, réessayer s'il vous plaît")
    return (int(size_number_horizontal),int(size_number_vertical), int(size_column))


def get_player_move(board):
    """ask and return the move the player want to play"""
    size_horizontal = board.width
    move_y = input("Où voulez-vous jouez ?\n position verticale ?")
    move_x = input("\n position horizontale ?")
    cond = 0
    while 1:
        if move_x.isdigit() and move_y.isdigit():
            move_x,move_y = int(move_x)-1,int(move_y)-1
            cond = move_x < 3 and move_x > 0 and move_y < 3 and move_y > 0
            if not(cond):
                break
        move_y = input("mouvement invalide ?\n position verticale ?")
        move_x = input("\n position horizontale ?")

    return (move_x,move_y)
