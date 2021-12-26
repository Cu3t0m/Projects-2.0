#  _  ______    Author: Kishore Satheeskumar
# | |/ / ___|   File: OOP-tutorial.py 
# | ' /\___ \   Description: Python Script for me to work through tutorials about OOP in Python
# | . \ ___) |  Links for tutorials: https://www.datacamp.com/community/tutorials/python-oop-tutorial
# |_|\_\____/   https://realpython.com/python3-object-oriented-programming/#classes-vs-instances
#               https://www.programiz.com/python-programming/object-oriented-programming


class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Bark function, self explanatory
    def bark(self):
        print("bark bark!")
    
    # Function that returns the information of object
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    # Function that adds 1 to value self.age
    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

# Defines objects based on class "Dog"
ozzy = Dog("Ozzy", 2)
# print(ozzy.name + " is " + str(ozzy.age) + " year(s) old.")
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

"""
# Calls the bark function defined in class "Dog"
# ozzy.bark()

# Returns info about the dog based off of function "doginfo", defined in the Dog class
ozzy.doginfo()
skippy.doginfo()
filou.doginfo()"""

ozzy.setBuddy(filou)

print(ozzy.buddy.doginfo())