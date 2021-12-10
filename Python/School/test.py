"""import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
"""

import random
import turtle as t

# Defining window dimensions and colour of stars
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
STAR_COLOUR="white"

t.Screen().screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().setworldcoordinates(-SCREEN_WIDTH,-SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().bgcolor("black")

"""
t.penup()
t.color(STAR_COLOUR, STAR_COLOUR)

t.goto(100,100)
t.dot(1)
t.goto(20,20)
t.dot(2)
t.goto(-100, -10)
t.dot(1)
t.goto(10,-100)
t.dot(1)
"""

# Random star co-ordinates
def random_star():
    t.penup()
    t.color(STAR_COLOUR, STAR_COLOUR)

    x = random.randint(-1000,1000)
    y = random.randint(-1000,1000)
    dot_size = random.random()*3

    t.goto(x,y)
    t.dot(dot_size)

for _ in range(1000):
    random_star()

t.hideturtle()
t.Screen().update()
