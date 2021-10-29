# Imports
from Hardware_Functions import *

# Choose difficulty
def menu():
    print("Welcome! If you feel confident in testing your knowledge of hardware, please enter 'yes' or 'y' when prompted, otherwise type 'no' or 'n'.")
    print("Answer:")
    menu.choice=input()

if menu.choice == "yes" or 'y':
    questions()
elif menu.choice == "no" or 'n':
    exit()
else:
    print("Invalid option, bringing you back to main menu.")
    menu()
menu()
