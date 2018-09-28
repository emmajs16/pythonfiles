# Emma Stoverink
# September 19, 2018
# Problem: rock paper sissors

import random
#get user's pick and randomly generate the computers pick
print("----------------------------------------------------------------")
print("{:^65}".format("ROCK, PAPER, SCISSORS"))
print("----------------------------------------------------------------")

user_pick = str(input("What do you pick? Please enter \"rock\", \"paper\", or \"scissors\":\n"))

if user_pick != "rock" or  user_pick != "paper" or user_pick != "scissors":
    user_pick = str(input("That is not an option. Please enter \"rock\", \"paper\", or \"scissors\":\n"))

computer_pick = random.randint(1,3)

if user_pick == "rock":
    user_pick = 1
elif user_pick == "paper":
    user_pick = 2
else:
    user_pick = 3

if user_pick == computer_pick:
    if user_pick == 1:
        user_pick = "rock"
    elif user_pick == 2:
        user_pick = "paper"
    else:
        user_pick = "scissors"
    print("There is a tie! You both chose {}.".format(user_pick))   
elif user_pick == 1:
    if computer_pick == 3:
        print("You chose rock and the computer chose scissors. You won.")
    elif computer_pick == 2:
        print("You chose rock and the computer chose paper. You lost!")
elif user_pick == 2:
    if computer_pick == 3:
        print("You chose paper and the computer chose scissors. You lost.")
    elif computer_pick == 1:
        print("You chose paper and the computer chose rock. You won!")
elif user_pick == 3:
    if computer_pick == 1:
        print("You chose scissors and the computer chose rock. You lost.")
    elif computer_pick == 2:
        print("You chose scissors and the computer chose paper. You won!")
    
