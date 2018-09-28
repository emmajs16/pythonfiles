## Emma Stoverink
## September 21, 2018
## Problem: Have the user guess heads or tails then filp a "coin" and tell if the user got it right or wrong.

import random

print("------------------------------------------")
print("|{:^40}|".format("Heads or Tails"))
print("------------------------------------------")

user_choice = str(input("Please choice \"heads\" or \"tails\":\n"))
if user_choice == "heads":
    user_choice = 1
else:
    user_choice = 0
    
computer_choice = random.randint(0,1)

if user_choice == computer_choice:
    print("You are correct!")
    if computer_choice == 1:
        computer_choice = "heads"
    else:
        computer_choice = "tails"
    print("You both chose {}.".format(computer_choice))
else:
    print("You are wrong...")
    if computer_choice == 1:
        computer_choice = "heads"
    else:
        computer_choice = "tails"
    print("The computer chose {}.".format(computer_choice))