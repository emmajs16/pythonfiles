# Emma Stoverink
# September 7, 2018
# Problem: Find the sum of all digits in an integer

# Get an integer from the user
user_number = int(input("Please enter an integer between 0 and 1000:"))

# Separate the digits and add it to a running total
sum = 0
sum += user_number % 10
user_number //= 10
sum += user_number % 10
user_number //= 10
sum += user_number % 10
user_number //= 10

# Display results
print(sum)