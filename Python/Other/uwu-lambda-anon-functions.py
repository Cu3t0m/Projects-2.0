add = lambda x, y : x + y
subtract = lambda x, y : x - y
multiply = lambda x, y : x * y
divide = lambda x, y : x / y

num1 = int(input('Number 1 '))
num2 = int(input('Number 2 '))
operator = input('Operator (+, -, x, /)')

if operator == '+':
    print(add(num1, num2))

elif operator == '-':
    print(subtract(num1, num2))

elif operator == 'x':
    print(multiply(num1, num2))

elif operator == '/':
    print(divide(num1, num2))

else:
    print('Invalid operator')