import random

def main():
    # Enter word to scramble
    word = input("Enter word: ")

    # Defining two lists, one for the word, the other for a new list that will be printed out later
    shuffle_list = list(word)
    new_list = []

    # Repeats for the amount of items in list "shuffle_list"
    for i in range(len(shuffle_list)):
        # Takes a random index from "shuffle_list" and assigns "changed_index" the value of 
        # the randomised index of "shuffle_list"
        shuffle_index = (random.randint(0, len(shuffle_list)-1))
        changed_index = shuffle_list[shuffle_index]
        # Removes the index randomly chosen, and appends "changed_index" to "new_list"
        shuffle_list.pop(shuffle_index)
        new_list.append(changed_index)
    
    # Prints out the original word and then the new word
    print("Original word:", word)
    print("The new word is: ","".join(new_list))

if __name__ == "__main__":
    main()