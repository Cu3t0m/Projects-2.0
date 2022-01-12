# Defining a dictionary that contains each playable tile
defBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

playable_board = []

for key in defBoard:
    playable_board.append(key)

# Board function to update the game status every time a move is made
def Board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Function play, which prints out the board and checks for whether or not there is a match of 3 characters
def play():

    turn = 'X'
    count = 0

    for i in range(10):
        Board(defBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if defBoard[move] == ' ':
            defBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if defBoard['7'] == defBoard['8'] == defBoard['9'] != ' ': # across the top
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif defBoard['4'] == defBoard['5'] == defBoard['6'] != ' ': # across the middle
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif defBoard['1'] == defBoard['2'] == defBoard['3'] != ' ': # across the bottom
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif defBoard['1'] == defBoard['4'] == defBoard['7'] != ' ': # down the left side
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif defBoard['2'] == defBoard['5'] == defBoard['8'] != ' ': # down the middle
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif defBoard['3'] == defBoard['6'] == defBoard['9'] != ' ': # down the right side
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif defBoard['7'] == defBoard['5'] == defBoard['3'] != ' ': # diagonal
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif defBoard['1'] == defBoard['5'] == defBoard['9'] != ' ': # diagonal
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If the number of total turns reaches 9 and there is no winner, 
        if count == 9:                
            print("You drew!\n")
            print("\nGame Over\n")
            print("Thanks for playing!")

        # Changes player after each move is done
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Asks players if they wish to restart or not
    restart = input("Do want to play Again? ")
    if restart == "y" or restart == "Y" or restart == "yes" or restart == "Yes":   
        for key in playyable_board:
            defBoard[key] = " "

        play()

play()