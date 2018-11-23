This file describe how to add a game to the library with the normalization that should be used for maximum compatibility

In this file xxx is the name of your game

# I. How to create the game:

  * Create a folder in src/games named game_xxx
  * In it place these files:
    * __init__.py which can be blank
    * board_xxx.py if the board needs to be initialized (i.e. 2048 needs 2 tiles at the beginning) with the function that will be needed to do it
    * player_interaction_xxx.py which states how the game will ask the player which move he wants to play
    * init_game_xxx.py in which you set every attribute of the Game() object that will hold your game as done in the 2048 example (it will be explained later)
    * rules_xxx.py which describes with functions the rules of the game, it is essential that this file contains four crucial functions:
      * make_a_move(board, move): both update and return the board according to the move specified
      * move_effective(board): return the list of the moves that will have an effect on the game (i.e. if all the tiles are on the left on 2k48 you can't go left)
      * is_over(board): return True if the game is over, else return False
      * calc_score(list_board, current_player): return the score of the current_player (can be 1 or 0 whether he has win or the score like in 2048)

# II. How to initialize a Game() object :

  * in init_game_xxx.py in your game folder create a function create_xxx() which should look like this :

        def create_xxx(new_game, args):
           new_game.name = "xxx"
           new_game.score = [0 for i in range(players_number)]
           new_game.list_board = [board_xxx.init_board(Board(4,4)) for i in range(players_number)]
           new_game.list_player = [i for i in range(players_number)]
           new_game.board_size = (4,4)
           new_game.move_available = [0,1,2,3] #list of the input available
           new_game.is_over_function = rules_xxx.is_over
           new_game.make_a_move_function = rules_xxx.make_a_move
           new_game.move_description = player_interaction_xxx.move_description # ex :"d : droite, g : gauche, h : haut, b : bas" what would be displayed to help the player uderstand what input corresponds to which move
           new_game.map_input_to_move = {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
           new_game.map_move_to_input = {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
           new_game.is_board_equal = False #set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
           new_game.next_turn_function = rules_xxx.create_new_tile
           new_game.calc_score_function = rules_xxx.calc_score
           new_game.move_effective_function = rules_xxx.move_effective

  * update the init_game() function in src.games.games.py to add the choice for your game like for the other games using the create_xxx() function defined in init_game_xxx.py in your game folder

# III. How to run a game alone:

  * use a script like this one (more examples can be found is example_init_game.py):
    ````xxx_game = init_game("xxx")
    while 1:
       print("joueur", xxx_game.player_playing)
      print(xxx_game.list_board[0].grid_to_string_with_size(3))
      move = player_interaction_p4.get_player_move(xxx_game.list_board[0])
      xxx_game.make_a_move(move)
      if not(xxx_game.is_over()[0]):
        xxx_game.next_turn()
        xxx_game.change_player()
      else:
        print("Le joueur ",  xxx_game.player_playing, "gagne")
        break```


# IV. Game() attributes:

  * name = name of the game
    * list_board = list of the boards (one for each players)
    * score = list of the scores
    * list_player = list of the id of players (0,1,2,...)
    * move_available = list of the inputs available
    * board_size = tuple (vertical_size, horizontal_size)
    * is_over_function = the function is_over of your game
    * make_a_move_function = the function make_a_move of your game
    * move_description = what should be displayed to help the player understand what input corresponds to which move
    * map_input_to_move = convert input to move number i.e. {'h' : 0,'d' : 1,'b' : 2,'g' : 3}
    * map_move_to_input = convert move number to input i.e. {0 : 'h',1 : 'd',2 : 'b',3 : 'g'}
    * is_board_equal = set it to true if the board of both player must be the same (i.e. in the Puissance 4 game)
    * theme_number = theme_number if needed (deprecated)
    * player_playing = id of the player which is currently playing
    * next_turn_function = the function next_turn of your game
    * calc_score_function = the function calc_score of your game
    * max_char_size = the size of the biggest character that will be used to display the board (i.e. 4 for 4096, 5 for 16384)
    * move_effective_function = the function move_effective of your game

# V. Add your game to the tournament : 
 
Now that your game is fully functional, you should make it accessible from the tournament, to do so :
  * At the top of the code of the file /exe.py, add the name of your game to the list "listeGames"
  * In the file /src/tournament.py next to the functions import_2048 etc. add a function with the following syntax
```
def import_xxx(self) :
    import src.games.game_xxx.player_interaction_xxx
    self.player_interaction = src.games.game_xxx.player_interaction_xxx
    import src.games.game_xxx.rules_xxx
    self.rules = src.games.game_xxx.rules_xxx
```
* Now in /src/tournament.py, in the function Gchoose_game add the following lines at the end 
```
elif game == "xxx":
    self.game_name = "xxx"
    self.import_xxx()
```
  * There, now your game should be accessible from within the tournament.
