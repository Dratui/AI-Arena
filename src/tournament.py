import operator
import src.players as player
import src.games.games as games


class Tournament:
    """This is the class that is going to manage tournaments, it includes all necessary information"""
    number_players = 0
    game_name = "" #Holds the name of the game
    list_players = []
    score=[] #score[i] holds the number of matches that player i has won
    leaderboard=[] #Leaderboard[i] hold the rank of player i.
    #The following three hold the modules that correspond to the game being played
    grid = None
    player_interaction = None
    rules = None
    game = games.Game()
    matches = [[]] #Is a nested list where matches[x][y] is an integer where -1 means the game between players x and y has not been played yet and otherwise this integer being the winner of the match
    
    def tournament_init(self):
        """Starts a new tournament, retrieving all relevant information on the game and the players"""
        self.number_players = int(input("How many players are there in this tournament ? (IA included) : "))
        self.list_players = select_player(self.number_players) #We create the list of all players of the Player class.
        self.game_name = input("What game are we going to play ? 'p4' ou '2048' ? ")
        while self.game_name != "2048" and self.game_name != "p4":
            self.game_name = input("Not a valid game, try again : ")
        if self.game_name == "2048": #Import of all relevant function to the game
            self.import_2048
        if self.game_name == "p4": #Same
            self.import_p4
        self.score = [0] * self.number_players
        matches = []
        for i in range(self.number_players): #Here we create the matrix for all 1 one 1 match.
            tempRow=[-1]*self.number_players
            matches.append(tempRow)
        self.matches = matches
        
    def import_2048(self):
        """Imports the game 2048 into the attributes of self"""
        import src.games.game_2048.grid_2048
        self.grid = src.games.game_2048.grid_2048
        import src.games.game_2048.player_interaction_2048
        self.player_interaction = src.games.game_2048.player_interaction_2048
        import src.games.game_2048.rules_2048
        self.rules = src.games.game_2048.rules_2048

    def import_p4(self):
        """Imports the game p4 into the attributes of self"""
        import src.games.game_p4.grid_p4
        self.grid = src.games.game_p4.grid_p4
        import src.games.game_p4.player_interaction_p4
        self.player_interaction = src.games.game_p4.player_interaction_p4
        import src.games.game_p4.rules_p4
        self.rules = src.games.game_p4.rules_p4
        
    def launch_a_game(self, player0, player1, display_ai_game = False):
        """Starts a game of the tournament, takes into argument the index of the two players, and display_ai_game which states if the games with only AIs must be displayed"""
        self.game = games.init_game(self.game_name)
        while not self.game.is_over()[0]:
            if display_ai_game or "human" in self.list_players[player0].name + self.list_players[player1].name: #If there is at least one human or if we have decided to watch the human players, we show them
                print(self.game.display_board())
            next_move = self.list_players[self.game.player_playing].get_move(self.game.list_board[self.game.player_playing],self.game) #We retrieve the move that the current player wants to make.
            self.game.make_a_move(next_move)
            if not self.game.is_over()[0]:
                self.game.next_turn()
                self.game.player_playing = (self.game.player_playing + 1) % self.number_players
        #Next part updates the scores and the values of matches
        if self.game.score[0] > self.game.score[1]:
            self.score[player0] += 1
            self.matches[player1][player0] = player0
            self.matches[player0][player1] = player0
        elif self.game.score[1] > self.game.score[0]:
            self.score[player1] += 1
            self.matches[player0][player1] = player1
            self.matches[player1][player0] = player1
        else:
            self.score[player0] += .5
            self.score[player1] += .5
            self.matches[player0][player1] = "ex aequo"
            self.matches[player1][player0] = "ex aequo"
            
        self.leaderboard = calculate_leaderboard(self.score)
        
    def launch_tournament(self,display_ai_game = False):
        """This function launches a tournament and manages the launching of the games, prints who wins every time and finally displays the leaderboard"""
        for x in range(self.number_players):
            for y in range(x+1, self.number_players): #These loops launch every possible game between two players and counts the number of win for each player
                self.launch_a_game(x,y,display_ai_game)
                if self.matches[x][y] != "ex aequo":
                    print("The winner is ", self.list_player, "\n")
                else:
                    print(self.matches[x][y],"\n")
        self.print_leaderboard(self.leaderboard)
                    
    def print_leaderboard(self, leaderboard):
        """This function prints the leaderboard, line by line, showing the name of the players and their rank"""
        print("RANKING : \n")
        for i in range(self.number_players):
            current_best, current_rank = max(enumerate(leaderboard), key=operator.itemgetter(1))
            print(self.list_players[current_best].name, " is number ", current_rank, "\n")
            leaderboard[current_best] = 0
            
            
        
        
        
        
        
def select_player(number_player):   
    """Asks a human who every player is, whether a human of the name of an AI"""
    list_player = [player.Player()] * number_player
    number_human_players = 1
    for i in range(1,number_player+1):
        temp_player = input("State the name of the IA for the player number {} (simply state h for a human player) : ".format(i))
        if temp_player == "h": #If we have a human, we wish to give a different name to them
            list_player[i-1].is_ai = False
            temp_player = "human_" + str(number_human_players)
            number_human_players += 1
            list_player[i-1].name = temp_player
            list_player[i-1].file = "human_ia"
        else:
            list_player[i-1].name = temp_player
            list_player[i-1].is_ai = True
            list_player[i-1].file = temp_player
    return list_player
    
def calculate_leaderboard(score):
    """Recieves the list of the score of every player and returns the rank of each player"""
    size = len(score)
    copy_score=score
    leaderboard = [0]*size
    index_of_max, current_max = max(enumerate(copy_score), key=operator.itemgetter(1)) #The index of the max value and said max value
    current_rank = 1
    current_rank_without_equal = 1 #This variable will always be incremented as it will give the value current_rank must take after managing two players with the same rank (E.G. to have 1,1,3 as ranks and not 1,1,2)
    while 0 in leaderboard:
        leaderboard[index_of_max] = current_rank
        copy_score[index_of_max] = -1
        index_of_max, current_max_temp = max(enumerate(copy_score), key=operator.itemgetter(1))
        current_rank_without_equal += 1
        if current_max_temp != current_max:
            current_max = current_max_temp
            current_rank = current_rank_without_equal
    return leaderboard
