'''
# Setting the variable 'flavour', giving it a value of 0 to be used later
flavour = 0
# Setting number of each ice cream flavour
numberOfVanilla = 0
numberOfChocolate = 0
numberOfStrawberry = 0
while flavour != "E":
    print("Select which flavour of ice cream you want, V, C, S or enter 'E' to exit the program")
    flavour = str(input())
    # Adds 1 to the numberOf(flavourName) 
    if flavour == "V":
        print("That's one Vanilla ice cream added to your cart")
        numberOfVanilla += 1
    elif flavour == "C":
        print("That's one Chocolate ice cream added to your cart")
        numberOfChocolate += 1
    elif flavour == "S":
        print("That's one Strawberry ice cream added to your cart")
        numberOfStrawberry += 1
    # When flavour is E, print out total number of ice cream bought and exit
    elif flavour == "E":
        # You can have this as a whole string I'm just formatting it like this for purposes of the screenshot
        print("You bought:")
        print(numberOfVanilla, "vanilla ice cream")
        print(numberOfChocolate, "chocolate ice cream")
        print(numberOfStrawberry, "strawberry ice cream")
'''

birds = ["Robin", "Chaffinch", "Blackbird", "Dove", "Sparrow"]
count = [1028, 1274, 1003, 1167, 1392]

# birds_str = x for x in birds
# count_str = x for x in count
for i in range(len(birds)):
    for x in birds:
        birds_str = x

    for x in count:
        count_str = x

    print(birds_str, "has a count of", count_str)