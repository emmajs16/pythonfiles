# Emma Stoverink
# September 7, 2018
# Problem: Calculate the tip and total for the user

# Get tip rate and the subtotal from the user
subtotal = float(input("\tPlease enter your subtotal:"))
tip_rate = int(input("\tPlease enter what percentage you would like to tip:")) /100

# Calculate the tip
tip = int((subtotal * tip_rate)*100)/100

# Calculate the total cost
total = int(((subtotal + tip) * 100))/100

# Display results
print("Subtotal : $", subtotal)
print("Tip : $", tip)
print("Total : $", total)