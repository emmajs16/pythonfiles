# Emma Stoverink
# September 7, 2018
# Problem: Input a number of minutes and output the number of years and days

# get the number of minutes from the user
minutes = int(input("Please enter the a number of minutes:"))

# convert the minutes into years by going from hours to days
hours = minutes // 60
total_days = hours // 24
years = total_days // 365

# find the days remaining
days_remaining = total_days%365

# display results
print(years,"years")
print(days_remaining,"days")
