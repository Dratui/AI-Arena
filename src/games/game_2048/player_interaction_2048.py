from src.games.game_2048.themes import THEMES

move_description = "d : droite, g : gauche, h : haut, b : bas\n"



def player_setup_theme():
    """ask and return the theme wanted by the player"""
    theme_number = input("Rentrez le numéro du thème que vous souhaitez avoir")
    if not(theme_number in THEMES.keys()):
        theme_number = input("Numéro invalide, réessayer s'il vous plaît")
    return int(theme_number)

def player_setup_size():
    """ask and return the size of the grid wanted by the player"""
    size_number = input("Rentrez la taille de grille que vous souhaitez avoir")
    while size_number.isdigit() == False:
        size_number = input("Entrée invalide, réessayer s'il vous plaît")
    return int(size_number)


def get_player_move():
    """ask and return the direction wanted by the player, 0 : up, 1 : right, 2 : down, 3 : left """
    direction = input("Dans quelle direction voulez-vous jouez ? (d : droite, g : gauche, h : haut, b : bas)")
    while not(direction in ["d","g","h","b"]):
        direction = input("Direction invalide, reéssayez (d : droite, g : gauche, h : haut, b : bas)")
    move = ["h","d","b","g"].index(direction)
    return move
