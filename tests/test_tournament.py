import src.tournament as tournament


tournoi = tournament.Tournament()
tournoi.number_players = 4
tournoi.game_name = "2048"
tournoi.score = [0,0,0,0]
tournoi.tournament_score = [0,0,0,0]
leaderboard = []
grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
tournoi.import_2048()
matches = []
for i in range(tournoi.number_players):
    tempRow=[-1,-1,-1,-1]
    matches.append(tempRow)
tournoi.matches = matches

def test_calculate_leaderboard():
    assert tournament.calculate_leaderboard([5,2,4,9,3,1,5,4,6,1,3,5,7,8,5]) == [5, 13, 9, 1, 11, 14, 5, 9, 4, 14, 11, 5, 3, 2, 5]
    assert tournament.calculate_leaderboard([1,1]) == [1,1]
    
def test_Gselect_players():
    global tournoi
    tournoi6 = tournoi
    tournoi6.Gselect_players(["h", "ai_2048_1", "h", "random_ai"])
    assert tournoi6.list_players[0].name == "human_1"
    assert tournoi6.list_players[2].name == "human_2"
    assert tournoi6.list_players[1].name == "ai_1_ai_2048_1"
    assert tournoi6.list_players[3].name == "ai_2_random_ai"
    
    assert tournoi6.list_players[0].is_ai == False
    assert tournoi6.list_players[2].is_ai == False
    assert tournoi6.list_players[1].is_ai == True
    assert tournoi6.list_players[3].is_ai == True
    
tournoi.Gselect_players(["ai_2048_1", "ai_2048_1", "ai_2048_1", "random_ai"])

def test_Gtournament_init():
    global tournoi
    tournoi2 = tournoi
    tournoi2.matches[0][1] = 1
    tournoi2.score[0] = 1
    tournoi2.tournament_score[0] = 1
    tournoi2.Gtournament_init(4)
    assert tournoi2.score == [0,0,0,0]
    assert tournoi2.tournament_score == [0,0,0,0]
    assert tournoi2.matches == [[-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]]
    
def test_reset_score():
    global tournoi
    tournoi3 = tournoi
    tournoi3.score[0] = 1
    tournoi3.reset_score()
    assert tournoi3.score == [0,0,0,0]
    
    
def test_launch_a_game():
    global tournoi
    tournoi5 = tournoi
    tournoi5.launch_a_game(1,3)
    assert tournoi5.matches[3][1] != -1
    assert tournoi5.matches[1][3] != -1
    assert tournoi5.leaderboard != []