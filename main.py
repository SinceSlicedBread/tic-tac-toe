import random
from Board import Board

## Initialise the game board and welcome message
game = Board()
game.start_game()

## Create players as lists for their inputs
player_1 = {'name': 'Player 1', 'marker': 'X', 'player_list': []}
player_2 = {'name': 'Player 2', 'marker': '0', 'player_list': []}

def take_turn(player, marker):
    choice = int(input(f"Choose a numbered block to mark with {marker}: "))
    if choice in player_1['player_list'] or choice in player_2['player_list']:
        print(f"Sorry, block {choice} has already been chosen. Please choose another block.")
        take_turn(player, marker)
    else:
        player.append(choice)
        game.update_board(choice=choice, marker=marker)

## While loop to run game
while game.game_on:
## Take player input (1-9) and add to game board (blank?)
    print("Player 1's turn")
    take_turn(player_1['player_list'], player_1['marker'])
    game.check_winner(player_1)
    if not game.game_on:
        break
    print("Player 2's turn")
    take_turn(player_2['player_list'], player_2['marker'])
    game.check_winner(player_2)

print("Thank you for playing my Tic Tac Toe game!")
