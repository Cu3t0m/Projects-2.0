# Imports
import time


# Questions for the quiz
def Q1():
        print ("Question 1:")
        print ("What's the CPU's purpose?")
        print("""Is it:
        [1] To store data
        [2] To create or remove data
        [3] To process data""")
        Q1.ans1 = int(input())

def Q2():
    print ("Question 2")
    print ("Which part of the CPU controls the flow of data?")
    print("""Is it:
    [1] The Arithmetic Logic Unit
    [2] The Immediate Access Store (cache)
    [3] The Control Unit""")
    Q2.ans2 = int(input())

def Q3():
        print("Question 3")
        print("What is one of the Von Neumann Architecture's advantages?")
        print("""Is it:
        [1] It's cheaper
        [2] It's smaller
        [3] It's faster""")
        Q3.ans3 = int(input())

def Q4():
        print("Question 4")
        print("What is clock speed?")
        print("""Is it:
        [1] How many FDE cycles can be executed in a second
        [2] How many times data can be moved across the buses per second
        [3] Data transfer speed""")
        Q4.ans4 = int(input())

def Q5():
        print("Question 5")
        print("How is clock speed measured?")
        print("""Is it:
        [1] GB
        [2] MB
        [3] GHz""")
        Q5.ans5 = int(input())

def Q6():
        print("Question 6")
        print("What is the immediate access store used for?")
        print("""Is it:
        [1] Storing files and programs
        [2] Storing data & programs the CPU needs at that moment
        [3] Storing random programs/files""")
        Q6.ans6 = int(input())

def endOfTest():
        print("""That's the end of the quiz!
        Out of 6, your score is""", test.TotalScore)
        print("Thanks for going through this quiz!")

# Function to call each question and uses several consecutive if/else statements to calculate your score at the end of the test
def test():
    print("""Hello! This quiz will test you on your knowledge of the CPU,
    you will be presented with a question, accompanied by a number.
    All you need to do to answer the question is enter the number next to your desired answer.""")
    print("Good luck! You will receive your score at the end")
    test.TotalScore = 0
    time.sleep(1)
    Q1()
    #If/else statments to verify your answer and reward points based off of it
    if Q1.ans1 == 3:
            print("Well done! You got the question right!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            Q2()
    else:
            print("Too bad! You got the question wrong!")
            test.TotalScore = test.TotalScore
            time.sleep(0.8)
            Q2()
    
    if Q2.ans2 == 3:
            print("Correct!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            Q3()
    else:
        print("Wrong!")
        test.TotalScore = test.TotalScore
        time.sleep(0.8)
        Q3()
    
    if Q3.ans3 == 1 or 3:
            print("Correct!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            Q4()
    else:
        print("Wrong!")
        test.TotalScore = test.TotalScore
        time.sleep(0.8)
        Q4()
    
    if Q4.ans4 == 1:
            print("Correct!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            Q5()
    else:
        print("Wrong!")
        time.sleep(0.8)
        Q4()
    
    if Q5.ans5 == 3:
            print("Correct!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            Q6()
    else:
        print("Wrong!")
        test.TotalScore = test.TotalScore
        time.sleep(0.8)
        Q6()
    
    if Q6.ans6 == 2:
            print("Correct!")
            test.TotalScore = test.TotalScore + 1
            time.sleep(0.8)
            endOfTest()
    else:
            print("Wrong!")
            test.TotalScore = test.TotalScore
            time.sleep(0.8)
            endOfTest()

def start_menu():
        print("Welcome to the quiz!")
        print("Before we start testing your knowledge, I would just like to make sure you really want to do the test, so answer with yes if you would like to carry on.")
        print("Answer with y or n depending on your choice")
        start_menu.answer = input()

        if start_menu.answer == "y":
                test()
        
        elif start_menu.answer == "n":
                exit()
        
        else:
                print("Invalid answer, returning to main menu.")
                start_menu()

start_menu()