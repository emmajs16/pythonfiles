# Emma Stoverink
# September 26, 2018
# Lottery Problem

import random

# Get the two guesses
user_number = int(input("Please enter a two digit integer:\n"))
random_number = random.randint(10,99)

# Make each digit individual
user_number1 = user_number // 10
user_number2 = user_number % 10
random_number1 = random_number // 10
random_number2 = random_number % 10

print("The lottery number is {}".format(random_number))
if user_number == random_number:
    print("Match both digits in order: you win $10,000!")
elif user_number1 + user_number2 == random_number1 + user_number2:
    print("Match both digits out of order: you win $5,000!")
elif (user_number1 == random_number1) or (user_number1 == random_number2) or (user_number2 == random_number1) or (user_number2 == random_number2):
    print("Match one digit: you win $1,000!")
else:
    print("Sorry, no match :(")