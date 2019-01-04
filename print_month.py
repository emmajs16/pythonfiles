# Emma Stoverink
# November 14, 2018

# Enter a year
# Enter a month
# Output calendar for that month

from calendar_functions import *
while True:
    year = input("Enter four digit year (e.g. 2001): ")
    if not year.isdigit():
        print("That's not a year!")
        print("Try again!!")
        continue
    if len(year) != 4:
        print("That is not four digits!")
        print("Try again!!")
    else:
        year = int(year)
        break
month = int(input("Enter month as a number between 1 and 12: "))

print(get_month(month))