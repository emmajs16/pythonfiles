## Emma Stoverink
## September 21, 2018
## Problem: Sort three integers from the user

print("------------------------------------------")
print("|{:^40}|".format("Sort three integers!"))
print("------------------------------------------")

print("\tPlease enter three different integers.")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

print("\tHere are your numbers in order!")
# if num1 is the smallest number
if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1)
        print(num2)
        print(num3)
    else:
        print(num1)
        print(num3)
        print(num2)
# if num2 is the smallest number
if num1 > num2 and num2 < num3:
    if num1 < num3:
        print(num2)
        print(num1)
        print(num3)
    else:
        print(num2)
        print(num3)
        print(num1)
# if num3 is the smallest number
if num3 < num1 and num3 < num2:
    if num1< num2:
        print(num3)
        print(num1)
        print(num2)
    else:
        print(num3)
        print(num2)
        print(num1)
        