# Imported libraries
import random

# Test 1
def test1():
  test1.test1Score = int(input("Enter your score for the first test: "))
  test1.test1UpperLimit = 15

  if test1.test1Score <= test1.test1UpperLimit:
    print("Valid score, submitting...")
    results = test1.test1Score
    test2()

  elif test1.test1Score > test1.test1UpperLimit:
    print("Invalid score, try again")
    test1()

# Test 2
def test2():
  test2.test2Score = int(input("Enter your score for the second test: "))
  test2.test2UpperLimit = 20


  if test2.test2Score <= test2.test2UpperLimit:
    print("Valid Score, submitting...")
    results2 = test2.test2Score
    exit()

  elif test2.test2Score > test2.test2UpperLimit:
    print("Invalid score, try again...")
    test2()

# Calling the program
test1()