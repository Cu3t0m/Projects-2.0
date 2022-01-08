# Function that acts as a template for each question
def questions(qnum, shape, height, width, option1, option2, option3):
    questions.score = int()

    print("Question "+str(qnum))
    print("What is the area of a", shape, "with dimensions", height, "cm by", width, "cm")
    print("Your options are:")
    print("1. "+str(option1)+" cm²")
    print("2. "+str(option2)+" cm²")
    print("3. "+str(option3)+" cm²")
    print("Enter your choice: ")

    questions.userans = int(input())

    if questions.userans == 1:
        questions.finalans = option1

    elif questions.userans == 2:
        questions.finalans = option2

    elif questions.userans == 3:
        questions.finalans = option3

    print("Your answer is", questions.finalans)

    true_ans = height*width

    if questions.finalans == true_ans:
        print("Well done!")
        questions.score += 1

    else:
        print("Too bad")

# rectangles_test function to be called in main menu
def rectangles_test():
    print("Welcome to the Rectangles test!")
    print("\n")
    print("This test is comprised of 5 questions, each testing your knowledge on the area of a rectangle.")
    print("Alright, the test starts now. At the end, you will get your score.")
    print("Ready? Start!")

    questions(1, "rectangle", 10, 4, 14, 40, 24)
    questions(2, "rectangle", 5, 15, 50, 65, 75)
    questions(3, "rectangle", 7, 6, 42, 39, 76)
    questions(4, "rectangle", 10, 12, 100, 190, 120)
    questions(5, "rectangle", 15, 12, 180, 200, 145)    

    print("Well done! you've completed the test.")
    print("At the end of it all, your score was: "+str(questions.score))
    print("\nThanks for playing!")

# triangles_test function to be called in main menu
def triangles_test():
    print("Welcome to the Triangles test!")
    print("\n")
    print("This test is comprised of 5 questions, each testing your knowledge on the area of a triangle.")
    print("Alright, the test starts now. At the end, you will get your score.")
    print("Ready? Start!")

    questions(1, "triangle", 12, 6, 36, 40, 24)
    questions(2, "triangle", 8, 10, 40, 32, 28)
    questions(3, "triangle", 10, 6, 33, 30, 24)
    questions(4, "triangle", 10, 12, 60, 56, 80)
    questions(5, "triangle", 15, 12, 100, 90, 80)    

    print("Well done! you've completed the test.")
    print("At the end of it all, your score was: "+str(questions.score))
    print("\nThanks for playing!")

# Main menu
print("Welcome! Select which area test you would like to take.")
print("""
Your options are:
1. Rectangles
2. Triangles
""")
print("Enter R for Rectangles, enter T for Triangles, or X to exit")
choice = input()

# Selection statement for each choice
if choice == "R":
    rectangles_test()

elif choice == "T":
    triangles_test()

elif choice == "X":
    print("Exiting the program...")
    exit()