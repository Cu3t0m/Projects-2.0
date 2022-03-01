list_of_numbers_to_find = [22, 14, 35, 15, 200, 33]
number_to_find = 14
for i in range(len(list_of_numbers_to_find)):
    if list_of_numbers_to_find[i] == number_to_find: 
        print(f"Number {number_to_find} found!")
        quit()
    else:
        print("Number not found. Trying again")

else:
    print(f"Number {number_to_find} couldn't be found")
