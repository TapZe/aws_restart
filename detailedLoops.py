"""
Working with Loops
"""

import random

# Exercise 1
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
# Exercise 2
print("Count to 10!")
for x in range(1, 11):
    print(x)

# Extra
number = input("Count 1 until .... :")
for x in range(1, int(number)+1):
    print(x)
