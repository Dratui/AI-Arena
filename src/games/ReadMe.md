The main functions needed to initialize the game objects are :
    - is_over : returns a tuple, with the first item being True if the game is over, and False if it is not and the second being the player that win
    - make_a_move : modifies the board according to a move given in args but don't return it
    - next_turn : modifies the board according to what is supposed to happen when a player finishes his turn but don't return it (i.e. 2k48 --> spawn a new tile)
    - move_effective : returns the list of the move that will have an efect on the game (i.e. not the move that will do nothing)
    - display_board : returns the string used to display the board

Normalization:
    - is_over : mandatory args = board, optional : player
                return = (is the game over (bool), which player has win (int)) (tuple)


    - make_a_move : args = board, move, player
                    return = updated board (Board)

                    Also update the board attribute from the game object



    - next_turn : args : None
                  return None

                  Update the board at the end of each turn


    - move_effective : args : board
                       return : list of the move that would have an effect (list)


Game implemented :
  - 2048 :
