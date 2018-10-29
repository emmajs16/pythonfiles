# Emma Stoverink
# October 26, 2018

# Coin flips
import random
heads = 0
tails = 0
flips = 1000000
for i in range (0,flips):
    current_flip = random.randint(0,1)
    if current_flip == 0:
        heads +=1
    else:
        tails+=1
print("You flipped {}% heads and {}% tails.".format(heads/flips*100, tails/flips*100))

    