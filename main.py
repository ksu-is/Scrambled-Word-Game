
import random 

# This is the word bank for level one
first_word = ['fun', 'ran', 'tan']
a= random.choice(first_word)
jumble = ''.join(random.sample(a,len(a)))
print(f"Welcome to the Scrambled Word Game! You will be presented a word to unscramble to move up in the three levels! You're starting on level 1: The Scrambled Word Is {jumble} ")


user_word = input("Guess the word: ")

if user_word == first_word:
    print("Incorrect! ")
else:
    print("Correct! Move on to level 2! ")
    pass

second_word = ['alert', 'brief', 'cycle']
b= random.choice(second_word)
jumbletwo= ''.join(random.sample(b,len(b)))
print(f"The Scrambled Word Is {jumbletwo}")

user_word= input("Guess the word: ")

if user_word == second_word:
    print("Incorrect! ")
else:
    print("Correct! Move on to the last level! ")
    pass

third_word = ['computer', 'average', 'information']
c = random.choice(third_word)
jumblethree = ''.join(random.sample(c,len(c)))
print(f"The Scrambled Word Is {jumblethree}")

user_word = input ("Guess the word: ")

if user_word == third_word:
    print("Incorrect!")
else:
    print("Correct! Congratulations, You have won the word scramble game! ")
quit()

 

