import operator

class Tournament:
    """This is the class that is going to manage tournaments, it includes all necessary information"""
    number_players = 0
    game = "" #Holds the name of the game
    list_players_who_is=[] #This list gives the list of players (with the number of each player being the position in the list) and states the corresponding AI or human
    score=[] #score[i] holds the number of matches that player i has won
    leaderboard=[] #Leaderboard[i] hold the rank of player i.
    #The following three hold the modules that correspond to the game being played
    grid = None
    player_interaction = None
    rules = None
    matches = [[]] #Is a nested list where matches[x][y] is an integer where -1 means the game between players x and y has not been played yet and otherwise this integer being the winner of the match
    
    def tournament_init(self):
        """Starts a new tournament, retrieving all relevant information on the game and the players"""
        self.number_players = int(input("How many players are there in this tournament ? (IA included) : "))
        self.list_players = select_player(self.number_players)
        self.game = input("What game are we going to play ? 'puissance4' ou '2048' ? ")
        while self.game != "2048" and self.game != "puissance4" :
            self.game = input("Not a valid game, try again : ")
        if self.game == "2048" : #Import of all relevant function to the game
            import_2048(self)
        if self.game == "p4" : #Same
            import_p4(self)
        self.score = [0] * self.number_players
        matches = []
        for i in range(self.number_players) :
            tempRow=[-1]*self.number_players
            matches.append(tempRow)
        
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
        
        
def select_player(number_player):
    """Asks a human who every player is, whether a human of the name of an AI"""
    who_is_player = []
    number_human_players = 1
    for i in range(1,number_player+1):
        temp_player = input("State the name of the IA for the player number {} (state h for a human player) : ".format(i))
        if temp_player == "h" :
            temp_player = "human_"
            temp_player += str(number_human_players)
            number_human_players += 1
        who_is_player.append(temp_player)
    return who_is_player
    
def calculate_leaderboard(score):
    """Recieves the list of the score of every player and returns the rank of each player"""
    size = len(score)
    copy_score=score
    leaderboard = [0]*size
    index_of_max, current_max = max(enumerate(copy_score), key=operator.itemgetter(1)) #The index of the max value and said max value
    current_rank = 1
    current_rank_without_equal = 1 #This variable will always be incremented as it will give the value current_rank must take after managing two players with the same rank (E.G. to have 1,1,3 as ranks and not 1,1,2)
    while 0 in leaderboard :
        leaderboard[index_of_max] = current_rank
        copy_score[index_of_max] = -1
        index_of_max, current_max_temp = max(enumerate(copy_score), key=operator.itemgetter(1))
        current_rank_without_equal += 1
        if current_max_temp != current_max :
            current_max = current_max_temp
            current_rank = current_rank_without_equal
    return leaderboard
        