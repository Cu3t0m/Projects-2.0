#!/usr/bin/env python3

# Object Oriented Programming.py

# Imports
import random

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