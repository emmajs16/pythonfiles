# Emma Stoverink
# November 7, 2018

import random

def roll_pair_dice(sides):
    roll = random.randint(1,sides) + random.randint(1,sides)
    return(roll)

def main():
    sides = int(input("How many sides are on your dice? "))
    player1 = roll_pair_dice(sides)
    player2 = roll_pair_dice(sides)
    print("Player 1 rolled a {} and Player 2 rolled a {}.".format(player1,player2))
    if player1 > player2:
        print("Player 1, you win!")
    elif player2 > player1:
        print("Player 2, you win!")
    else:
        print("There is a tie!")
        
main()
