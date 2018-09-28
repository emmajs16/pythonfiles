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
# if both numbers are the same
if user_number == random_number:
    print("Match! Both digits in order: you win $10,000!")
# if both digits match but the order is switched
elif (user_number1 == random_number1) or (user_number1 == random_number2) and (user_number2 == random_number1):
    print("Match! Both digits out of order: you win $5,000!")
# if one digit matches
elif (user_number1 == random_number1) or (user_number1 == random_number2) or (user_number2 == random_number1) or (user_number2 == random_number2):
    print("Match! One digit: you win $1,000!")
# if no numbers match each other
else:
    print("Sorry, no match :(")