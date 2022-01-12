print("Hiya")
import time
#Arjun Gill and Aadiththan Yogeswaran
#Assigns players using conditions and a while loop to ensure the input is valid
def choices(player1name,player2name,naughts,crosses):
  assign=0
  while assign==0:
   player1name=str(input("What is player 1's name: "))
   player2name=str(input("What is player 2's name: "))
   naughts=input("Who is naughts: ")
   if naughts==player1name:
     print("naughts is", player1name, "and crosses is", player2name)
     assign=1
   elif naughts==player2name:
     print("naughts is", player2name, "and crosses is", player1name)
     assign=1
   else:
     print("Invalid, try again")
     assign==0

#Makes the grid by using 3 lists for the rows and joins them with a gridline
def grid(rows):
 rows = [[".",".","."],[".",".","."],[".",".","."]]
 print('|'.join(rows[0]))
 print("-+-+-")
 print('|'.join(rows[1]))
 print("-+-+-")
 print('|'.join(rows[2]))

def game(win,turns,move,xmoverow1,xmovecol1,rows):
  while win==0 and turns < 9:
    for y in range (9):
      move=1
      if move==1:
       xmoverow1=int(input("Please choose the row for your X, note the numbers start from 0: "))
       if xmoverow1==1:
         xmovecol1=int(input("Please choose the column for your X: "))
         rows[xmoverow1][xmovecol1]="X"
         print('¦'.join(rows[0]))
         print('¦'.join(rows[1]))
         print('¦'.join(rows[2]))
       else:
         print("")
      else:
        print("")

player1name=str("")
player2name=str("")
naughts=str("")
crosses=str("")
assign=int(0)
row1=str("")
row2=str("")
row3=str("")
rows = [[".",".","."],[".",".","."],[".",".","."]]
win=int(0)
turns=int(0)
move=int(1)
xmoverow1=int()
xmovecol1=int()

choices(player1name,player2name,naughts,crosses)
grid(rows)
game(win,turns,move,xmoverow1,xmovecol1,row1,row2,row3)