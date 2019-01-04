# Emma Stoverink
# November 9, 2018

def display_sorted_numbers(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            return("{} {} {}".format(num1,num2,num3))
        if num2 > num3:
            return("{} {} {}".format(num1,num3,num2))
    if num1 > num2 and num1 < num3:
        if num2 < num3:
            return("{} {} {}".format(num2,num1,num3))
        if num2 > num3:
            return("{} {} {}".format(num3,num2,num2))
    else:
        if num2 < num3:
            return("{} {} {}".format(num2,num3,num1))
        if num2 > num3:
            return("{} {} {}".format(num3,num2,num1))

def main():
    x, y, z = input("Enter three numbers: ").split()
    print("The three sorted numbers are: {}".format(display_sorted_numbers(x,y,z)))

    
main()