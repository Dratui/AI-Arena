from src.games.games import Game

def ia_output(board,game): #the ia's output corresponds to the human input
    output=input(game.move_description)
    while output not in [str(game.map_move_to_input[i]) for i in range(len(game.move_available))]: #intput verification
        output=input(game.move_description)
    return(game.map_move_to_input[output])




