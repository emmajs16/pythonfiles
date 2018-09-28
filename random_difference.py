# Emma Stoverink
# September 16, 2018

# Problem: print if the inputted difference of two numbers is true or false
import random

a = random.randint(1,9)
b = random.randint(1,9)

if b>a:
    a,b = b,a
    
difference = int(input("What is the difference between {}-{}? \n".format(a,b)))
if a-b==difference:
    print("You are so smart!! {} minus {} is equal to {}! Good job! :)".format(a,b, difference))    
else:
    print("You are wrong...{}minus {} is NOT equal to {}. The correct answer is {}. :(".format(a,b,difference,(a-b)))