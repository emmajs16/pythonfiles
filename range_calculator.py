# Emma Stoverink
# September 12, 2018

# Make a range calculator for a car

# Get user input for initial variables
odometer_initial = int(input("Enter the initial odometer reading:"))
gallons_total = int(input("Enter the gallons of gas your tank holds:"))
odometer_second = int(input("Enter the second odometer reading:"))
gallons_left = int(input("Enter the gallons left in your tank:"))

# Find the mpg
gallons_used = gallons_total - gallons_left
miles_traveled = odometer_second - odometer_initial
miles_per_gallon = miles_traveled / gallons_used

# Find how many more miles the car can go
miles_left = gallons_left * miles_per_gallon

# Output results
print("You can travel "+ str(miles_left)+ " more miles before you need to refuel!")