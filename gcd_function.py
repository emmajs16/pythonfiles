# Emma Stoverink
# November 12

def gcd(num1,num2):
    if num2 > num1:
        num1,num2 = num2,num1
    for i in range(1,num2+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

##def main(x,y):
##    print("The GCD of {} and {} is {}".format(x,y,gcd(x,y)))
##    
##main(10,20)