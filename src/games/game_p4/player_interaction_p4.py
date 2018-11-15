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


def get_player_move(size_horizontal, grid):
    """ask and return the move the player want to play"""
    move = input("Où voulez-vous jouez")
    print(type(move))
    cond = True
    if move.isdigit():
        cond  = not(int(move)-1 < size_horizontal and int(move)-1 >= 0) or grid[0][int(move)] != " "

    while cond:
        move = input("Coup non valide, recommencez")
        cond = True
        if move.isdigit():
            cond  = not(int(move) -1 < size_horizontal and int(move) -1 >= 0) or grid[0][int(move)] != " "

    return int(move)-1
