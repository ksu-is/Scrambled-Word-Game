
import random 

# This is the word bank for level one
first_word = ['fun', 'run', 'tan']
a = random.choice(first_word)
jumble = ''.join(random.sample(a,len(a)))
print(f"the jumbled word is {jumble}")


user_word = input("Guess the word: ")

if user_word == first_word:
    print("Incorrect!")
else:
    print("Correct! Move on to level 2!")

breakpoint

second_word = ['alert', 'brief', 'cycle']
b = random.choice(second_word)
jumbletwo = ''.join(random.sample(b,len(b)))
print(f"the jumbled word is {jumbletwo}")

user_word = input("Guess the word: ")

if user_word == second_word:
    print("incorrect!")
else:
    print("Correct! Move on to the last level!")

breakpoint

third_word = ['computer', 'average', 'information']
c = random.choice(third_word)
jumblethree = ''.join(random.sample(c,len(c)))
print(f"the jumbled word us {jumblethree}")

user_word = input ("Guess the word: ")

if user_word == third_word:
    print("Incorrect!")
else:
    print("Correct! You have won the word scramble game!")

breakpoint

 

