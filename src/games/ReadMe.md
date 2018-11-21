The main functions needed to initialize game objects are :

    - is_over : returns a tuple, with the first item being True if the game is over, and False if it is not and the second being the player that win

    - make_a_move : modifies the board according to a move given in args but don't return it

    - next_turn : modifies the board according to what is supposed to happen when a player finishes his turn but don't return it (i.e. 2k48 --> spawn a new tile)

    - move_effective : returns the list of the move that will have an effect on the game (i.e. not the move that will do nothing)

    - display_board : returns the string used to display the board

Normalization:

    - is_over : mandatory args : board, optional : player
                return : (is the game over (bool), which player has win (int)) (tuple)


    - make_a_move : args : board, move, player
                    return : updated board (Board)

                    Also update the board attribute from the game object


    - next_turn : args : None
                  return : None

                  Update the board at the end of each turn


    - move_effective : args : board
                       return : list of the move that would have an effect (list)

    - An exemple of a game initialization can be found in the init_game_xxxx.py inside the folders of the three games that are already implemented


Game already implemented :

    - 2048 :

        - moves : 0 for up
                  1 for right
                  2 for down
                  3 for left

      - p4 :

          - moves : number of the column (starting from 0)

      - ttt :

          - moves : number of the tile (0 to 8)
                    |0|1|2|
                    |3|4|5|
                    |6|7|8|
