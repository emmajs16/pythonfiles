def m(i):
    result = 0
    for value in range(1,i+1):
        fraction = (-1**(value+1))/(2*value-1)
        if value %2 == 1:
            result -= fraction
        if value %2 == 0:
            result += fraction
##        result *=4
        print(result)

m(901)