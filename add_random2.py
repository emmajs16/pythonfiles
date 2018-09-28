# Emma Stoverink
# September 16, 2018

# Problem:  if the inputted sum of two numbers is true print a message

import random

a = random.randint(1,9)
b = random.randint(1,9)
sum = int(input("What is the sum of {} + {}? \n".format(a,b)))
if a+b==sum:
    print("You are so smart!! {} plus {} is equal to {}! Good job! :)".format(a,b, sum))
##if a+b!=sum:    
else:
    print("You are wrong...{} plus {} is NOT equal to {}. :(".format(a,b, sum))