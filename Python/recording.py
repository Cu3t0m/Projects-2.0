# Imports
import sys

# Defining functions for each mathematical operator
def add(x,y):
    answer = x+y
    return answer

def subtract(x,y):
    answer = x-y
    return answer

def multiply(x,y):
    answer = x*y
    return answer

def divide(x,y):
    answer = x/y
    return answer

# Generating user input for each number used and the operator
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter your chosen operator (add, subtract, multiply, divide)")


# Which operator is used based on input
if operator == "add":
    add(num1,num2)
    sys.exit()

elif operator == "subtract":
    subtract(num1, num2)
    sys.exit()

elif operator == "multiply":
    multiply(num1, num2)
    sys.exit()

elif operator == "divide":
    divide(num1, num2)
    sys.exit()

else:
    print("invalid operator...")
    sys.exit()
