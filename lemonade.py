# Emma Stoverink
# September 14, 2018
# Lemonade Stand
import math
# Get user input
cost_rent = float(input("How many dollars is the rent for your stand?"))
cost_materials = int(input("How many cents are the materials per glass?"))/100
cost_per_glass = int(input("How many cents are you charging per glass?"))/100
profit = float(input("What is your profit goal in dollars?"))

# profit = cost per glass*x - (rent + material cost * x)
# find x, the number of cups sold to make the certain profit

cups_to_sell = math.ceil(abs((profit + cost_rent) / (cost_materials- cost_per_glass)))
print("You must sell {} cups of lemonade to reach your profit goal of ${:.2f}.".format(cups_to_sell, profit))

