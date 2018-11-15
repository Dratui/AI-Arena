#import src.board as brd
#import src.player as plr


class tournament:
    number_players = 0
    game = ""
    list_players_who_is=[]
    leaderboard=[[]]
    
    def tournament_init(self):
        self.number_players = int(input("How many players are there in this tournament ? (IA included) : "))
        self.list_players = select_player(self.number_players)
        self.game = input("What game are we going to play ? ")

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
    


