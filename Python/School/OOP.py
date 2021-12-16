#!/usr/bin/env python3

# Object Oriented Programming.py

# Imports
import random
import time

# Defining a class, this will be used later
class player_Pokemon():
  def __init__(self,name="",strength="",hp="",maxHP="",level=""):
    self.name = name
    self.strength = strength
    self.hp = hp
    self.maxHP = maxHP
    self.level = level

  def character_profile(self):
    print("Your Pokemon:\n")
    print("Name: ",self.name)
    print("Level: ",self.level)
    print("Strength: ",self.strength)
    print("HP: ",self.hp,"/",self.maxHP)

class enemy_Pokemon():
    def __init__(self,ename="",estrength="",ehp="",emaxHP="",elevel=""):
        self.ename = ename
        self.estrength = estrength
        self.ehp = ehp
        self.emaxHP = emaxHP
        self.elevel = elevel
    
    def enemy_profile(self):
        print("Your enemy:\n")
        print("Name: ",self.ename)
        print("Level: ",self.elevel)
        print("Strength: ",self.estrength)
        print("HP: ",self.ehp,"/",self.emaxHP)

# Defining functions
def RNG(x,y):
  damageMultiplier = random.randint(0,10)
  return damageMultiplier


# Defines the player and enemy's properties, like health, strength, level, etc. and prints out a profile
playerPokemon = player_Pokemon()
playerPokemon.name = "Pikachu"
playerPokemon.strength = 9
playerPokemon.hp = 40
playerPokemon.maxHP = 40
playerPokemon.level = 5
playerPokemon.character_profile()

enemyPokemon = enemy_Pokemon()
enemyPokemon.ename = "Charmander"
enemyPokemon.estrength = 5
enemyPokemon.ehp = 40
enemyPokemon.emaxHP = 40
enemyPokemon.elevel = 5
enemyPokemon.enemy_profile()

BATTLEOVER = False

while BATTLEOVER is False:

    print("Current battle status:")
    print("You:")
    print(playerPokemon.character_profile())
    time.sleep(0.5)
    print("Your opponent:")
    print(enemyPokemon.enemy_profile())
    time.sleep(0.5)

    dmg_mod = RNG(0,10)
    damage_mod = dmg_mod + playerPokemon.strength
    enemyPokemon.ehp = enemyPokemon.ehp - damage_mod

    dmg_mod = RNG(0, 10)
    enemy_damage_mod = dmg_mod + enemyPokemon.estrength
    playerPokemon.hp = playerPokemon.hp - enemy_damage_mod
    time.sleep(0.5)

    YOUWON = 0
    # (Testing) Different message depending on variable "YouWon"
    if playerPokemon.hp > 0 and enemyPokemon.ehp <= 0:
        YOUWON = True

    elif playerPokemon.hp <= 0 and enemyPokemon.ehp > 0:
        YOUWON = False

    # if either fighter's health is lower than 0 then program ends
    if playerPokemon.hp <= 0 or enemyPokemon.ehp <= 0:
        print("The battle is over, thanks for playing!")
        if YOUWON is True:
            print("You won! Great job!")
        else:
            print("You lost...try again next time")

        time.sleep(0.5)
        BATTLEOVER = True

    # BATTLEOVER = True
