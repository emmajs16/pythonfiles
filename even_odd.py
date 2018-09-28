# Emma Stoverink
# September 16, 2018

# Problem:  find if a number is even or odd

a = int(input("Please enter a number:\n"))
even = a % 2 == 0
if even==True:
    print("{} is an EVEN number.".format(a))
##if even==False:
else:
    print("{} is an ODD number.".format(a))