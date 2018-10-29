# Emma Stoverink
# October 24, 2018

# Tuition increase

tuition = 10000
year = 0

while tuition < 20000:
    tuition *= 1.07
    year+=1
    
print("In {} years, tuition will be ${:.2f}, which is greater than $20,000.".format(year,tuition))

##x = 1.0
##x -= .1
##x -= .1
##x -= .1
##x -= .1
##x -= .1
##print(x)