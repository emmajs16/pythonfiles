# Emma Stoverink
# October 24, 2018

# Find the smallest factor of an integer other than 1

user_int = int(input("Enter an integer: "))

for i in range(2, user_int):
    if user_int % i == 0:
        smallest_factor = i
        break
    
print("The smallest factor of {} is {}.".format(user_int, smallest_factor))