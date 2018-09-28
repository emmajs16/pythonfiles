# Emma Stoverink
# September 16, 2018

# Problem: print if the inputted sum of two numbers is true or false

import random

a = random.randint(1,9)
b = random.randint(1,9)
sum = int(input("What is the sum of {} + {}? \n".format(a,b)))
print("{}+{}={} is {}.".format(a,b,sum,a+b==sum))
