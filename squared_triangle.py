# Emma Stoverink
# October 29, 2018

value = 1
i = 2
for row in range (1, 9):
    for row in range(1,10-i):
        print("  ",end="  ")
    for row in range (1,i):
        print("{:>3}".format(value), end = " ")
        value *= 2
    value //=2
    for row in range(i,2,-1):
        value //= 2
        print("{:>3}".format(value), end = " ")
    print()
    i+=1  
    
