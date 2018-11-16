

class Tournament:
    """This is the class that is going to manage tournaments, it includes all necessary information"""
    number_players = 0
    game = "" #Holds the name of the game
    list_players_who_is=[] #This list gives the list of players (with the number of each player being the position in the list) and states the corresponding AI or human
    leaderboard=[]
    #The following three hold the modules that correspond to the game being played
    grid = None
    player_interaction = None
    rules = None
    
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
        self.leaderboard = [(0,i) for i in range(self.number_players)]
        
        
    def import_2048(self):
        import src.games.game_2048.grid_2048
        self.grid = src.games.game_2048.grid_2048
        import src.games.game_2048.player_interaction_2048
        self.player_interaction = src.games.game_2048.player_interaction_2048
        import src.games.game_2048.rules_2048
        self.rules = src.games.game_2048.rules_2048

    def import_p4(self):
        import src.games.game_p4.grid_p4
        self.grid = src.games.game_p4.grid_p4
        import src.games.game_p4.player_interaction_p4
        self.player_interaction = src.games.game_p4.player_interaction_p4
        import src.games.game_p4.rules_p4
        self.rules = src.games.game_p4.rules_p4
        
        
def select_player(number_player):
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
    



