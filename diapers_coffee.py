# Emma Stoverink
# September 14, 2018

# Diapers or Coffee Problem

# Set constant variables
DAYS_PER_MONTH = 30
COFFEE_CALORIES = 490
CALORIES_PER_POUND = 3500

# Get user input
diapers_cost = float(input("What is the cost of a dozen diapers? "))
diapers_per_day = int(input("How many diapers does the baby go through a day? "))
coffee_cost = float(input("What is the cost of a single caramel frappuccino? "))

# Find the total cost of diapers per month, the frappaccinos saved per month,the calories saved, and the pounds lost
diaper_total_cost = (diapers_per_day * DAYS_PER_MONTH)* (diapers_cost / 12)
coffee_saved = int(diaper_total_cost / coffee_cost)
calories_saved = coffee_saved * COFFEE_CALORIES
pounds_lost = calories_saved/ CALORIES_PER_POUND

# print results
print("You will spend ${:.2f} on diapers a month".format(diaper_total_cost))
print("You will drink {} fewer frappuccinos each month.".format(coffee_saved))
print("As a result, you will loose {:.2f} pounds in a month".format(pounds_lost))