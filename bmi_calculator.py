## Emma Stoverink
## September 21, 2018
## Problem: Calculate the BMI of a user

#Constants
METERS_PER_INCH = 0.0254
KILOS_PER_POUND = 0.45359237

#User input
weight_pound= int(input("Please enter your weight in pounds: "))
print("Please enter your height in feet and inches.")
height_feet = int(input("\tFeet: "))
height_inch = int(input("\tInches: "))

# Convert pounds to kilos
weight_kilos = weight_pound * KILOS_PER_POUND

# convert height to meters
height_inch += height_feet*12
height_meters = height_inch * METERS_PER_INCH

# Calculate BMI
bmi = weight_kilos / (height_meters**2)

print("Results:")
print("Your BMI is {:.2f}.".format(bmi))
if bmi > 30:
    interpretation = "obese"
elif bmi >= 25:
    interpretation = "overweight"
elif bmi >= 18.5:
    interpretation = "normal"
else:
    interpretation = "underweight"
    
print("-Your results are {}.".format(interpretation))