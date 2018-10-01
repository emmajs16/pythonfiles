# Emma Stoverink
# October 1, 2018

#Keep asking a subtraction problem until the user gets it right

import random
a = random.randint(1,9)
b = random.randint(1,9)

if b>a:
    a,b = b,a

print("Please answer the following:\n")
difference = int(input("\t{} - {} = ".format(a,b)))

while a-b != difference:
    print("\nThat is incorrect. Please try again: \n")
    difference = int(input("\t{} - {} = ".format(a,b)))
print("\nYou got it!\n")
