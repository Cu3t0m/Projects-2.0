# Imports
import time

# Questions
def Q1():
        print ("Question 1:")
        print ("How does data travel from the memory to the CPU?")
        print("""Is it:
        [1] Through the address bus
        [2] Through the data bus
        [3] Throught the main memory""")
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

def endOfTest():
        print("""That's the end of the quiz!
        Out of 5, your score is""", test.TotalScore)
        print("Thanks for going through this quiz!")

# Computing revision: CPU
def test():
    print("""Hello! This quiz will test you on your knowledge of the CPU,
    you will be presented with a question, accompanied by a number.
    All you need to do to answer the question is enter the number next to your desired answer.""")
    print("Good luck! You will receive your score at the end")

    test.TotalScore = 0
    time.sleep(5)
    Q1()
    
    #If/else statments to verify your answer and reward points based off of it
    if Q1.ans1 == 1:
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
        endOfTest()
    else:
        print("Wrong!")
        test.TotalScore = test.TotalScore
        time.sleep(0.8)
        endOfTest()

#Calling the actual program
test()