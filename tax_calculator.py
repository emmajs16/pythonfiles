# Emma Stoverink
# September 5, 2018
# Problem: Find the sales tax due on a certain amount to exactly two decimals

# Get the sales tax and the total amount spent before tax
tax_percent = 8
tax_rate = tax_percent / 100
amount_before_tax = float(input("Enter how much you spent before tax:"))
# Calculate the cost of tax
tax_cost = amount_before_tax * tax_rate                   
# Convert the total to just two decimal points
rounded_tax_cost = (round(tax_cost * 100))/100
# add up and round the total cost
total_cost = rounded_tax_cost + amount_before_tax
rounded_total_cost = (round(total_cost * 100))/100
#display the results
print("You need to pay $",rounded_tax_cost,"in tax so a total of $" , rounded_total_cost)