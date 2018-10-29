# Emma Stoverink
# October 5, 2018

# smallest n greater than 12000
##n = 0
##while (n*n) < 12000:
##    n+=1
##print("{} squared is {}.".format(n,n*n))

# largest n less than 12000

n = 0
while (n*n*n) <= 12000:
    n+=1
n-=1
print("{} cubed is {}.".format(n,n*n*n))
