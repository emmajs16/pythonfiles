# Emma Stoverink
# September 7, 2018
# Problem: change feet to meters

# CONSTANTS
FEET_PER_METERS = 0.305

# get length in feet from user
length_ft = int(input("Please enter a length in feet:"))

# convert length from feet to meters
length_m = length_ft * FEET_PER_METERS

# display results
print(length_ft, "feet is equal to", length_m, "meters.")