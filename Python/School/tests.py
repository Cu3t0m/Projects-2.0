"""import array as arr

myArray = arr.array('hello', [1.3, 2.4, 5.6])

print(myArray[0])"""

import pprint

def ThreeD(a, b, c):
    lst = [[ ['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst

col1 = 5
col2 = 3
row = 2

pprint.pprint(ThreeD(col1, col2, row))


