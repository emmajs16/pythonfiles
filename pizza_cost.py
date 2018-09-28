# Emma Stoverink
# September 14, 2018
# Pizza cost of medium or large

# MEDIUM PIZZA
import math
    # get user input
medium_diameter = int(input("What is the size (diameter) of a medium pizza in inches?"))
medium_cost = float(input("What is the cost of a medium pizza?"))
    
    # find area of the pizza and cost per square inch
medium_area = math.pi * ((medium_diameter/2)**2)
medium_cost_per_inch = medium_cost /medium_area

    # print results
print("The area of a {} inch medium pizza is {:.2f} inches.".format(medium_diameter, medium_area))
print("\t It will cost ${:.2f} per inch.".format(medium_cost_per_inch))

# LARGE PIZZA

    # get user input
large_diameter = int(input("What is the size (diameter) of a large pizza in inches?"))
large_cost = float(input("What is the cost of a large pizza?"))

    # find area of the pizza and cost per square inch
large_area = math.pi * ((large_diameter/2)**2)
large_cost_per_inch = large_cost /large_area

    # print results
print("The area of a {} inch large pizza is {:.2f} inches.".format(large_diameter, large_area))
print("\t It will cost ${:.2f} per inch.".format(large_cost_per_inch))

# COMPARE THE TWO PIZZAS

med_large_cost_difference = (large_cost_per_inch / medium_cost_per_inch)
print("The medium pizza is {:.2%} more expensive than the large pizza per inch.".format(med_large_cost_difference))