# Emma Stoverink
# October 26, 2018

# tution increase in 10 years and the cost of four years worth of tution in 10 years

tuition = 10000

for i in range(0,10):
    tuition *= 1.07
four_year_cost = 0
for i in range(0,4):
    tuition *= 1.07
    four_year_cost += tuition
print("In 10 years, you will have to pay ${:.2f} total for tution over four years.".format(four_year_cost))
