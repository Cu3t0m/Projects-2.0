# Coding  Task 2/12/2021

## Imports
import random
import time

## Defining functions for damage modification, the current state of the battle and the fights during the battle
def RNG(x,y):
    x = 0
    y = 10
    modifier = random.randint(x, y)
    return modifier

######## Defining pokemon you choose later ########
pokemon = [["Name", "Strength", "HP", "Max HP"],["Pikachu", 9, 40, 40],["Charmander", 5, 55, 55]]

###### Printing out a table in a nice format ######
mx = len(max((sub[0] for sub in pokemon), key=len))

for row in pokemon:
    print("|".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))

##### Choosing the Pokemon you fight with. #####
print("Which Pokémon would you like to battle?")
print("Enter 1 for Pikachu, 2 for Charmander")

# Choices
choice = int(input())

if choice == 1:
    print("You chose Pikachu!")
    playerChar = pokemon[1]
    enemyChar = pokemon[2]
    print("Your opponent: Charmander")

elif choice == 2:
    print("You chose Charmander!")
    playerChar = pokemon[2]
    enemyChar = pokemon[1]
    print("Your opponent: Pikachu")

# Starts the battle
BATTLEOVER = False

while BATTLEOVER is False:

    print("Current battle status:")
    print("You:")
    print("HP: ",playerChar[2],"/",playerChar[3])
    print("ATK: ",playerChar[1])
    print("\n\n")
    time.sleep(0.5)
    print("Your opponent:")
    print("HP: ",enemyChar[2],"/",enemyChar[3])
    print("ATK: ",enemyChar[1])
    time.sleep(0.5)

    dmg_mod = RNG(0,10)
    damage_mod = dmg_mod + playerChar[1]
    enemyChar[2] = enemyChar[2] - damage_mod

    dmg_mod = RNG(0, 10)
    enemy_damage_mod = dmg_mod + enemyChar[1]
    playerChar[2] = playerChar[2] - enemy_damage_mod
    time.sleep(0.5)

    YOUWON = 0
    # (Testing) Different message depending on variable "YouWon"
    if playerChar[2] > 0 and enemyChar[2] <= 0:
        YOUWON = True

    elif playerChar[2] <= 0 and enemyChar[2] > 0:
        YOUWON = False

    # if either fighter's health is lower than 0 then program ends
    if playerChar[2] <= 0 or enemyChar[2] <= 0:
        print("The battle is over, thanks for playing!")
        if YOUWON is True:
            print("You won! Great job!")
        else:
            print("You lost...try again next time")

        time.sleep(0.5)
        BATTLEOVER = True

    # BATTLEOVER = True
