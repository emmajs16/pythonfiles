## Emma Stoverink
## September 21, 2018
## Problem: Generate a random card for the user

import random

print("------------------------------------------")
print("|{:^40}|".format("Pick a Card!"))
print("------------------------------------------")

print("We will generate a random card for you\nfrom a standard deck of 52 cards.")

go = (input("Press \"ENTER\" to see your card!"))

rank = random.randint(1,13)
if rank == 1:
    rank = "Ace"
if rank == 11:
    rank = "Jack"
if rank == 12:
    rank = "Queen"
if rank == 13:
    rank = "King"
suit = random.randint(1,4)
if suit == 1:
    suit = "Clubs"
elif suit == 2:
    suit = "Diamonds"
elif suit == 3:
    suit = "Hearts"
else:
    suit = "Spades"
    
print("Your card is: The {} of {}.".format(rank,suit))
