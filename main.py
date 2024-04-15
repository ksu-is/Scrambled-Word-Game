import random

# This is the welcome screen code
def welcome():
    print("Welcome to the Word Scrambled Game!")
    print("There are three levels, to move through each level you will have to unscramble each word correctly.")
    print("Enjoy unscrambling!")
    input("Press Enter to Start!")
print()

# This is the word bank 
word = ["fun", "alert", "computer"]

letters = list(word)
random.shuffle(letters)
jumbled_word = "".join(letters)

While True:
    guess = input("Guess this scrambled word: ")
    if guess.lower() != word.lower():
        print("Incorrect, Please try again!")
    else:
        break
print("Correct! Move on to the  next level!")

 

