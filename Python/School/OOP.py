#!/usr/bin/env python3

# Object Oriented Programming.py

# Defining a class, this will be used later
class pokemon():
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

playerPokemon = pokemon()
playerPokemon.name = "Pikachu"
playerPokemon.strength = 10
playerPokemon.hp = 40
playerPokemon.maxHP = 40
playerPokemon.level = 5
playerPokemon.character_profile()