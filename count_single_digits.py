# Emma Stoverink
# November 30, 2018

# Count single digits

import random

list = []
for i in range(0,101):
    list.append(random.randint(0,9))

for i in range (0,10):
    print("There are {} number {}'s in the list.".format(list.count(i),i))