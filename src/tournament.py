import operator
import src.players as player
import src.games.games as games
from copy import copy
from tkinter import *
from graphics.graphic import update_display


class Tournament:
    """This is the class that is going to manage tournaments, it includes all necessary information"""
    number_players = 0
    game_name = "" #Holds the name of the game
    list_players = []
    score=[] #score[i] holds the temporary score of the players for the current game
    tournament_score=[] #Holds the number of games a player has won
    leaderboard=[] #Leaderboard[i] hold the rank of player i.
    #The following three hold the modules that correspond to the game being played
    grid = None
    player_interaction = None
    rules = None
    game = games.Game()
    matches = [[]] #Is a nested list where matches[x][y] is an integer where -1 means the game between players x and y has not been played yet and otherwise this integer being the winner of the match

    #Importations functions

    def import_2048(self):
        """Imports the game 2048 into the attributes of self"""
        import src.games.game_2048.player_interaction_2048
        self.player_interaction = src.games.game_2048.player_interaction_2048
        import src.games.game_2048.rules_2048
        self.rules = src.games.game_2048.rules_2048

    def import_p4(self):
        """Imports the game p4 into the attributes of self"""
        import src.games.game_p4.player_interaction_p4
        self.player_interaction = src.games.game_p4.player_interaction_p4
        import src.games.game_p4.rules_p4
        self.rules = src.games.game_p4.rules_p4

    def import_TicTacToe(self):
        """Imports the game Tic Tac Toe into the attributes of self"""
        import src.games.game_ttt.player_interaction_ttt
        self.player_interaction = src.games.game_ttt.player_interaction_ttt
        import src.games.game_ttt.rules_ttt
        self.rules = src.games.game_ttt.rules_ttt

    def Glaunch_a_game(self, player0, player1,window, display_ai_game = False, graphical_display = True):
        """Starts a game of the tournament, takes into argument the index of the two players, and display_ai_game which states if the games with only AIs must be displayed"""
        self.game = games.init_game(self.game_name)
        self.game.player_playing = 0
        while not self.game.all_over():
            if graphical_display and (display_ai_game or "human" in self.list_players[player0].name + self.list_players[player1].name): #If there is at least one human or if we have decided to watch the non-human players, we show them

                update_display(window,self.game)

            elif not graphical_display :
                print(self.game.display_board)
            if not self.game.is_over()[0]:
                if self.game.player_playing == 0 :
                    next_move = self.list_players[player0].get_move(self.game.list_board[0],self.game) #We retrieve the move that the current player wants to make.
                else :
                    next_move = self.list_players[player1].get_move(self.game.list_board[1],self.game)
                self.game.make_a_move(next_move)
                self.game.next_turn()
                self.game.score[self.game.player_playing] = self.game.calc_score()
            self.game.player_playing = (self.game.player_playing + 1) % 2
        #Next part updates the scores and the values of matches
        if self.game.score[0] > self.game.score[1]:
            self.tournament_score[player0] += 1
            self.matches[player1][player0] = player0
            self.matches[player0][player1] = player0
        elif self.game.score[1] > self.game.score[0]:
            self.tournament_score[player1] += 1
            self.matches[player0][player1] = player1
            self.matches[player1][player0] = player1
        else:
            self.tournament_score[player0] += .5
            self.tournament_score[player1] += .5
            self.matches[player0][player1] = "ex aequo"
            self.matches[player1][player0] = "ex aequo"
        self.reset_score()
        self.leaderboard = calculate_leaderboard(self.tournament_score)
        if graphical_display:
            if display_ai_game:
                self.game.window.quit()



    def Glaunch_tournament(self,display_ai_game = False, graphical_display = True):
        """This function launches a tournament and manages the launching of the games, prints who wins every time and finally displays the leaderboard"""
        for x in range(self.number_players):
            for y in range(x+1, self.number_players): #These loops launch every possible game between two players and counts the number of win for each player

                window=Tk()
                self.Glaunch_a_game(x,y,window,display_ai_game, graphical_display)
                window.destroy()
                window.mainloop()

                if self.matches[x][y] != "ex aequo":
                    print("The winner of a game between player ", self.list_players[x].name, " and player ", self.list_players[y].name, " is ", self.list_players[self.matches[x][y]].name, "\n")
                else:
                    print(self.matches[x][y],"\n")
        return self.print_leaderboard(self.leaderboard)



    def print_leaderboard(self, leaderboard):
        """This function prints the leaderboard, line by line, showing the name of the players and their rank"""
        txt=""
        for i in range(self.number_players):
            current_best, current_rank = max(enumerate(leaderboard), key=operator.itemgetter(1))
            if (self.list_players[current_best].file!="human"):
                txt+=self.list_players[current_best].name+" is number "+str(current_rank)+ "\n"
            else:
                txt+=self.list_players[current_best].file+" is number "+str(current_rank)+ "\n"
            leaderboard[current_best] = 0
        return txt

    def reset_score(self):
        self.score = []
        for _ in range(self.number_players):
            self.score.append(0)


    def Gtournament_init(self,number_players):
        """Starts a new tournament, retrieving all relevant information on the game and the players"""

        self.number_players=number_players
        self.score = []
        for _ in range(self.number_players):
            self.score.append(0)
        matches = []
        for i in range(self.number_players): #Here we create the matrix for all 1 one 1 match.
            tempRow=[-1]*self.number_players
            matches.append(tempRow)
        self.matches = matches
        self.tournament_score = []
        for _ in range(self.number_players):
            self.tournament_score.append(0)


    def Gchoose_game(self, game):
        """Function that select the game script depending on the game (string) entered"""
        if game=="2048":
            self.import_2048()
            self.game_name="2048"
        elif game=="Puissance 4":
            self.import_p4()
            self.game_name="p4"
        elif game == "TicTacToe":
            self.game_name = "ttt"
            self.import_TicTacToe()


    def Gselect_players(self,Glist_names):
        """Asks a human who every player is, whether a human of the name of an ai"""
        list_players = []
        for i in range(self.number_players) :
            list_players.append(player.Player())
        number_human_players = 1
        number_ai_players = 1
        for i in range(1,self.number_players+1):
            temp_player = Glist_names[i-1]
            if temp_player == "h": #If we have a human, we wish to give a different name to them
                list_players[i-1].is_ai = False
                temp_player = "human_" + str(number_human_players)
                number_human_players += 1
                list_players[i-1].name = temp_player
                list_players[i-1].file = "human"
            else:
                list_players[i-1].is_ai = True
                list_players[i-1].file = temp_player
                temp_player = "ai_" + str(number_ai_players) + "_" + temp_player
                list_players[i-1].name = temp_player
                number_ai_players += 1
        self.list_players=list_players

def calculate_leaderboard(score):
    """Recieves the list of the score of every player and returns the rank of each player"""
    size = len(score)
    copy_score=copy(score)
    leaderboard = []
    for _ in range(size):
        leaderboard.append(0)
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
