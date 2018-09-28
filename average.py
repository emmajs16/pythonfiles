# Emma Stoverink
# September 3, 2018
# Problem: get three values and find the average

def find_average():
    #get three values from the user
    num_1 = int(input("Please enter your first number:"))
    num_2 = int(input("Please enter your second number:"))
    num_3 = int(input("Please enter your third number:"))
    #add the values together
    sum = num_1 + num_2 + num_3
    # divide sum by number of values
    number_of_values = 3
    average = int(sum / number_of_values)
    #print results
    print("\tThe average of", num_1, ",", num_2, ", and", num_3, "is about", average)

find_average()