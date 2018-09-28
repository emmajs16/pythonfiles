number = int(input("Enter a number:\n"))
if number % 2 == 0 and number % 3 == 0:
    print("{} is divisible by 2 and 3.".format(number))
if number % 2 == 0 or number % 3 == 0:
    print("{} is divisible by 2 or 3.".format(number))
    if ((number % 2 == 0) and(number % 3 != 0)) or ((number % 3 == 0) and(number % 2 != 0)):
        print("{} is divisible by 2 or 3, but not both of them.".format(number))

