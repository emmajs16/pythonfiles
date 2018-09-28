# Name:
# Date:
#
# CSC 2280 - Lab 5: Nested Selection Practice

import random

print("*******************************************************")
print("***                  Math Practice                  ***")
print("*******************************************************")
print("* You can:                                            *")
print("*     1. Addition Practice                            *")
print("*     2. Subtraction Practice                         *")
print("*     3. Multiplication Practice                      *")
print("*     4. Division Practice                            *")
print("* Please enter your choice (1, 2, 3, or 4):")

user_choice = int(input())

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

# IF: ADDITION
if user_choice == 1:
    print("\n{}{:^35s}{}".format("++++++++++", "Addition Practice", "++++++++++"))
    sum = num1 + num2
    print("Please enter your answer:")
    user_answer =int(input("{} + {} = ".format(num1, num2)))
    if user_answer == sum:
        print("\nGreat job! Your answer is correct!")
    else:
        print("\nThat is not correct.")
        print("Here is the correct answer:")
        print("{} + {} = {}".format(num1, num2, sum))
        try_again = str(input("\nWould you like to try again? (Y or N)? "))
        if try_again.lower() == "y":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            sum = num1 + num2
            print("Please enter your answer:")
            user_answer =int(input("{} + {} = ".format(num1, num2)))
            if user_answer == sum:
                print("\nGreat job! Your answer is correct!")
            else:
                print("\nThat is not correct.")
                print("Here is the correct answer:")
                print("{} + {} = {}\n".format(num1, num2, sum))
                print("Keep trying! You'll get it!")
        else:
            print("\nNo problem. Goodbye.")
# ELSE IF: SUBTRACTION
elif user_choice == 2:
    print("\n{}{:^35s}{}".format("----------", "Subtraction Practice", "----------"))
    print("Please enter your answer:")
    if num1 < num2:
        num1,num2 = num2, num1
    user_answer =int(input("{} - {} = ".format(num1, num2)))
    difference = num1 - num2
    if user_answer == difference:
        print("\nGreat job! Your answer is correct!")
    else:
        print("\nThat is not correct.")
        print("Here is the correct answer:")
        print("{} - {} = {}".format(num1, num2, difference))
        try_again = str(input("\nWould you like to try again? (Y or N)? "))
        if try_again.lower() == "y":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            if num1 < num2:
                num1,num2 = num2, num1
            difference = num1 - num2
            print("Please enter your answer:")
            user_answer =int(input("{} - {} = ".format(num1, num2)))
            if user_answer == difference:
                print("\nGreat job! Your answer is correct!")
            else:
                print("\nThat is not correct.")
                print("Here is the correct answer:")
                print("{} - {} = {}\n".format(num1, num2, difference))
                print("Keep trying! You'll get it!")
        else:
            print("\nNo problem. Goodbye.")
# ELSE IF: MULTIPLICATION
elif user_choice == 3:
    print("\n{}{:^35s}{}".format("xxxxxxxxxx", "Multiplication Practice", "xxxxxxxxxx"))
    product = num1 * num2
    print("Please enter your answer:")
    user_answer =int(input("{} x {} = ".format(num1, num2)))
    if user_answer == product:
        print("\nGreat job! Your answer is correct!")
    else:
        print("\nThat is not correct.")
        print("Here is the correct answer:")
        print("{} * {} = {}".format(num1, num2, product))
        try_again = str(input("\nWould you like to try again? (Y or N)? "))
        if try_again.lower() == "y":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            product = num1 * num2
            print("Please enter your answer:")
            user_answer =int(input("{} x {} = ".format(num1, num2)))
            if user_answer == product:
                print("\nGreat job! Your answer is correct!")
            else:
                print("\nThat is not correct.")
                print("Here is the correct answer:")
                print("{} x {} = {}\n".format(num1, num2, product))
                print("Keep trying! You'll get it!")
        else:
            print("\nNo problem. Goodbye.")
# ELSE IF: DIVISION
elif user_choice == 4:
    print("\n{}{:^35s}{}".format("//////////", "Division Practice", "//////////"))
    print("Please enter your answer:")
    product = num1 * num2
    #have the user find the result of dividing the product by num1 to equal num2
    user_answer =int(input("{} / {} = ".format(product, num1)))
    if user_answer == num2:
        print("\nGreat job! Your answer is correct!")
    else:
        print("\nThat is not correct.")
        print("Here is the correct answer:")
        print("{} / {} = {}".format(product, num1, num2))
        try_again = str(input("\nWould you like to try again? (Y or N)? "))
        if try_again.lower() == "y":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            product = num1 * num2
            print("Please enter your answer:")
            user_answer =int(input("{} / {} = ".format(product, num1)))
            if user_answer == num2:
                print("\nGreat job! Your answer is correct!")
            else:
                print("\nThat is not correct.")
                print("Here is the correct answer:")
                print("{} / {} = {}\n".format(product, num1, num2))
                print("Keep trying! You'll get it!")
        else:
            print("\nNo problem. Goodbye.")

# ELSE: invalid choice
else:
    print("\nInvalid choice selected. Goodbye.")
