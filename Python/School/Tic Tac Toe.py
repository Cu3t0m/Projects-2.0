# Kishore and Anan
import sys

# defining a game board
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

# Gives the players the option to restart
def restart():
    restart_game = input("Do you want to play again? (y/n) ")
    if restart_game == "y" or restart_game == "Y":
        main()
    elif restart_game == "n" or restart_game == "N":
        print("Thank you for playing the game!")
        exit()

# Main function for the full game
def main():
    
    # Actual game, for 9 consecutive turns, players will be asked to enter 
    # a number from 1 to 9, allowing them to choose where their counter
    # is placed.
    current_turn = "x"
    turn_count = 0

    for i in range(10):
        print_board(dict_board)
        print("Hey " + current_turn + ", it's your go! Where do you want to\nput your marker?")
        player_move = input()

        # If the chosen tile is empty, replace that tile with the player's marker, 
        # or ask the player to re-enter if the tile is already taken.
        if dict_board[player_move] == ' ':
            dict_board[player_move] = current_turn
            turn_count += 1

        else:
            print("Sorry, that tile is already taken, choose a different one.")
            continue

        # Checking for 3 matching tiles after 5 moves (total)

        if turn_count >= 5:
        ## Each side
            if dict_board['7'] == dict_board['4'] == dict_board['1']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()

            if dict_board['7'] == dict_board['8'] == dict_board['9']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()

            if dict_board['9'] == dict_board['6'] == dict_board['3']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()

            if dict_board['1'] == dict_board['2'] == dict_board['3']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()

        ## Middle
            if dict_board['4'] == dict_board['5'] == dict_board['6']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()

        ## Both diagonals
            if dict_board['1'] == dict_board['5'] == dict_board['9']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()
            
            if dict_board['3'] == dict_board['5'] == dict_board['7']:
                print("\nGame Over!\n")
                print(current_turn + " won.")
                restart()
        
        # If the total turn count reaches 9, the game ends as a draw
        if turn_count == 9:
            print("\nGame Over!\n")
            print("It's a tie! Thanks for playing!")
            restart()

        # Switches between players after each move
        if current_turn == "x":
            current_turn = "o"
        else:
            current_turn = "x"


main()