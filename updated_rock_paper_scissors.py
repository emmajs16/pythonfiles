# Emma Stoverink
# October 24, 2018

# Continuous rock paper sissors

import random
#get user's pick and randomly generate the computers pick
print("----------------------------------------------------------------")
print("{:^65}".format("ROCK, PAPER, SCISSORS"))
print("----------------------------------------------------------------")
user_score = 0
computer_score = 0
while True:
    user_pick = str(input("What do you pick? Please enter \"rock\", \"paper\", or \"scissors\":\n"))

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
            user_score +=1
        elif computer_pick == 2:
            print("You chose rock and the computer chose paper. You lost!")
            computer_score +=1
    elif user_pick == 2:
        if computer_pick == 3:
            print("You chose paper and the computer chose scissors. You lost.")
            computer_score +=1
        elif computer_pick == 1:
            print("You chose paper and the computer chose rock. You won!")
            user_score +=1
    elif user_pick == 3:
        if computer_pick == 1:
            print("You chose scissors and the computer chose rock. You lost.")
            computer_score +=1
        elif computer_pick == 2:
            print("You chose scissors and the computer chose paper. You won!")
            user_score +=1
    print("Your score: {}.".format(user_score))
    print("The computer's score: {}.".format(computer_score))
    if computer_score - user_score == 3 or user_score - computer_score == 3:
        break
print()
print("The game is over.")
if  user_score > computer_score:
    print("You won!")
else:
    print("You lost...")