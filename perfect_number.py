# Emma Stoverink
# October 29, 2018
# Perfect number

print("Perfect numbers less than 10,000 include:")

for number in range(2, 10001):
    # reset the sum to 0
    sum = 0
    for value in range (1,(number//2)+1):
        # if the number is divisible by the value, add that value to the sum
        if number % value == 0:
            sum += value
    # if the sum and the number are equal, print
    if sum == number:
        print(number)