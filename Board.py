#Winning number combinations
h1 = [1,2,3]
h2 = [4,5,6]
h3 = [7,8,9]
v1 = [1,4,7]
v2 = [2,5,8]
v3 = [3,6,9]
d1 = [1,5,9]
d2 = [3,5,7]

class Board():
    def __init__(self):
        with open('board.txt') as file:
            self.display_board = file.read()
        self.score_board = self.display_board
        self.game_on = True

    def start_game(self):
        print('Welcome to Tic Tac Toe!\nPlease familiarise yourself with the gameboard:')
        print(self.display_board)

    def check_winner(self, player):
        if (len(set(h1).intersection(player['player_list'])) == 3
                or len(set(h2).intersection(player['player_list'])) == 3
                or len(set(h3).intersection(player['player_list'])) == 3
                or len(set(v1).intersection(player['player_list'])) == 3
                or len(set(v2).intersection(player['player_list'])) == 3
                or len(set(v3).intersection(player['player_list'])) == 3
                or len(set(d1).intersection(player['player_list'])) == 3
                or len(set(d2).intersection(player['player_list'])) == 3):
            print(f'{player["name"]} wins!')
            self.game_on = False
        return self.game_on

    def update_board(self, choice, marker):
        self.score_board = self.score_board.replace(str(choice), marker)
        print(self.score_board)
