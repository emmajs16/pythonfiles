# Emma Stoverink
# October 29, 2018

##for row in range(1, 7):
##    for i in range(6-row):
##        print(" ",end = " ")
##    for value in range (1, row):
##        if value % 2 == 0:
##            print(value, end = " ")
##        else:
##            print((value-1)*2, end = " ")
##    print()
##print()
for row in range(1, 7):
    for i in range(6-row):
        print(" ",end = " ")
    for value in range (1,row+1):
        print(value, end = " ")
##    for value in range (2, row+1):
##        print(value, end = " ")
    print()
print()

value = 1

for row in range (1,9):
    print(value)
    value *= 2
    
