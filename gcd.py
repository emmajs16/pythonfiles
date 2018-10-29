# Emma Stoverink
# October 22, 2018

#Greatest common denominator

n1 = int(input("Please enter an integer: "))
n2 = int(input("Please enter an integer: "))
gcd = 1
# if n1 is less than n2 switch the values
if n1 < n2:
    n1,n2 = n2,n1
# for each number between 2 and n2 check to see if it is divisible by each number
for i in range(2,n2+1):
    if n1 % i == 0 and n2 % i == 0:
        # if its true make the gcd equal to that value
        gcd = i
        
print("The GCD of {} and {} is {}.".format(n1,n2, gcd))
