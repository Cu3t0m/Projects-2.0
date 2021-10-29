#Imports
from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=1, scale_x=1)

def update():
    player.y += held_keys['w'] * .1
    player.y -= held_keys['s'] * .1
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1

#Opens window and runs program
app.run()