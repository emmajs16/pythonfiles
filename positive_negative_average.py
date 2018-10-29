# Emma Stoverink
# October 5, 2018

sum = 0
positives = 0
negatives = 0
count = 0
number = int(input("Enter an integer, the input ends when you enter 0: "))
while number != 0:
    number = int(input("Enter an integer, the input ends when you enter 0: "))
    sum += number
    count+=1
    if number > 0:
        positives+=1
    else:
        negatives +=1
if sum == 0:
    print("You didn't enter any numbers!")
else:
    print("The number of positive integers is {}.".format(positives))
    print("The number of negative integers is {}.".format(negatives))
    print("The total is {}".format(sum))
    print("The average is {:.2f}".format(sum/count))
    
