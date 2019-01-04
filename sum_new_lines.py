# Emma Stoverink
# November 26, 2018

numbers_to_enter = int(input("How many numbers do you want to enter? "))
print("\nGreat, please enter those {} numbers (one per line) below.\n".format(numbers_to_enter))
sum = 0

for i in range(numbers_to_enter):
    sum += int(input("Enter a number: "))
   
print("\nThe sum of the {} numbers entered is {}".format(numbers_to_enter, sum))
print("\nThe average of the {} numbers entered is {:.2f}.".format(numbers_to_enter, sum/numbers_to_enter))