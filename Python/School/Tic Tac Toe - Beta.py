# Kishore and Anan

# The game is playable and the win condition appears to be working.
# Some advice to improve your game could be to work on innovating the input system for your board.
# Peer reviewed by Zhaoqi

# * Fixes:
# * Error handling - Done
# * Out of bounds code - Done
# * Restart doesn't clear board - Done
# * Weird win conditions - Done
# * Fix Function to clear board when win condition is met - Done

# * Features to add:
# * Username - Done
# Point system - Ongoing
# AI - Haven't started
# Database for profiles - Haven't started

# Imports
import subprocess

# Defining a game board
dict_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


# Board function to update the game status every time a move is made
def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Function to clean board after game is over
def clean_board(board):
    for key in board:
        board[key] = ' '

# Function to update points for each player
# ! Doesn't update player points
def win_pts(playerturn, xpts, opts):
    if playerturn == 'x':
        xpts += 1
    
    elif playerturn == 'o':
        opts += 1

    return xpts, opts

# Defining player names
x_name = input("What's the name of player X? ")
o_name = input("What's the name of player O? ")

# Player points
x_pts = 0
o_pts = 0

# Main function for the full game
def main():
    
    # Actual game, for 9 consecutive turns, players will be asked to enter 
    # a number from 1 to 9, allowing them to choose where their counter
    # is placed.
    player_turn = "x"
    turn_count = 0
    
    current_player = x_name

    print("Player " + str(x_name) + "'s points: " + str(x_pts))
    print("Player " + str(o_name) + "'s points: " + str(o_pts))

    for i in range(10):
        print_board(dict_board)
        print("Hey " + current_player + ", it's your go! Where do you want to\nput your marker?")
        player_move = input()

        if player_move == '' or player_move == ' ':
            print("Try again, except enter a number between 1 and 9")
            continue

        # Checks to see if it's out of bounds
        elif int(player_move) > len(dict_board):
            print("Sorry! You're out of bounds.")
            continue
            
        else:
        # If the chosen tile is empty, replace that tile with the player's marker, 
        # or ask the player to re-enter if the tile is already taken.
            if dict_board[player_move] == ' ':
                dict_board[player_move] = player_turn
                turn_count += 1

            else:
                print("Sorry, that tile is already taken, choose a different one.")
                continue

        # Checking for 3 matching tiles after 5 moves (total)
        if turn_count >= 5:

            # Sides
            if dict_board['7'] == dict_board['8'] == dict_board['9'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            elif dict_board['1'] == dict_board['2'] == dict_board['3'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            elif dict_board['1'] == dict_board['4'] == dict_board['7'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            elif dict_board['3'] == dict_board['6'] == dict_board['9'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            # Middles
            elif dict_board['4'] == dict_board['5'] == dict_board['6'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            elif dict_board['2'] == dict_board['5'] == dict_board['8'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                

            # Diagonals
            elif dict_board['7'] == dict_board['5'] == dict_board['3'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
            elif dict_board['1'] == dict_board['5'] == dict_board['9'] != ' ':
                print_board(dict_board)
                print("\nGame Over.\n")
                print(current_player + " won.")
                break
                
                 
        # Switches between players after each move
        if player_turn == "x":
            player_turn = "o"
            current_player = o_name
        else:
            player_turn = "x"
            current_player = x_name

        # If the total turn count reaches 9, the game ends as a draw
        if turn_count == 9:
            print("\nGame Over!\n")
            print("It's a tie! Thanks for playing!")
            restart()
    
    # Gives the players the option to restart
    restart_game = input("Do you want to play again? (y/n) ")
    if restart_game == "y" or restart_game == "Y":
        clean_board(dict_board)
        subprocess.run("clear")
        main()

    elif restart_game == "n" or restart_game == "N":
        print("Thank you for playing the game!")
        subprocess.run("clear")
        exit()

# Cleans the board and then runs the main function
if __name__ == "__main__":
    clean_board(dict_board)
    main()