# Emma Stoverink
# November 12, 2018

from gcd_function import gcd

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))

print("The GCD of {} and {} is {}".format(num1,num2,gcd(num1,num2)))