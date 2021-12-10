## Task: Roman numerals

### Converts an integer into a Roman numeral

class romanNumerals:
  def RomanNumerals(self, num):
    val = [
      1000, 900, 500, 400,
      100, 90, 50, 40,
      10, 9, 5, 4,
      1
      ]
    syb = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
      "X", "IX", "V", "IV",
      "I"
      ]
    roman_num = ''
    i = 0
    while  num > 0:
      for _ in range(num // val[i]):
        roman_num += syb[i]
        num -= val[i]
      i += 1
    return roman_num
print(romanNumerals().RomanNumerals(int(input("Enter any random integer: "))))

## Tasks: Lists

print("Enter the first number")
startNumber = int(input())

print("Enter the end number")
endNumber = int(input())

numbers = []

for i in range(startNumber,endNumber):
  numbers.append(i)
  print(numbers)

## Task: Random Password Generator

import random
import string

passLength = int(input("Length of password: "))

letters = string.ascii_letters
print(''.join(random.choice(letters) for i in range(passLength)))

## Random password generator revised

passwordLength = random.randint(0,50)

typeOfPassword = random.randint(1,6)

if typeOfPassword == 1:
    passType = string.ascii_letters

elif typeOfPassword == 2:
    passType = string.ascii_lowercase

elif typeOfPassword == 3:
    passType = string.ascii_uppercase

elif typeOfPassword == 4:
    passType = string.digits

elif typeOfPassword == 5:
    passType = string.hexdigits

elif typeOfPassword == 6:
    passType = string.octdigits

print(''.join(random.choice(passType) for i in range(passwordLength)))

## Task: I Like Pi

import math

pi = 3.141592653589793238462643383279502884197
formattedText = f"{pi:.30f}"
Truncated_pi = float(text)

print(Truncated_pi)

## Task: Beautiful Soup

from bs4 import BeautifulSoup
import urllib2

url = "https://www.bbc.co.uk/news"

content = urllib2.urlopen(url).read()
soup = BeatifulSoup(content)

for link in soup.find_all('a'):
    print(link.get('href'))

## Task: Your name is

print("Enter your name:")
uname = str(input())

print("Enter your age:")
uage = int(input())

print("Enter your form:")
uform = input()

print("Your name is {}, you are {} years old, and you are in form {}".format(uname,uage,uform))
