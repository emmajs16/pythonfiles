# Emma Stoverink
# October 1, 2018

# Guess the computers number

import random

computer_number = random.randint(1,100)
print("Guess a number between 1 and 100.")
guess = int(input("Enter your guess: "))
while computer_number != guess:
    if guess > computer_number:
        print("Your guess is too high!")
        guess = int(input("Enter your guess: "))
    else:
        print("Your guess is too low!")
        guess = int(input("Enter your guess: "))
print("Yes! The number is {}!".format(computer_number))
