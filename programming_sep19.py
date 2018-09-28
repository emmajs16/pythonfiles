##n = int(input())
##if n >= 1 and n <= 12:
##    if n == 1:
##        print("January")
##    elif n == 2:
##        print("February")
##    elif n == 3:
##        print("March")
##    elif n == 4:
##        print("April")
##    elif n == 5:
##        print("May")
##    elif n == 6:
##        print("June")
##    elif n == 7:
##        print("July")
##    elif n == 8:
##        print("August")
##    elif n == 9:
##        print("September")
##    elif n == 10:
##        print("October")
##    elif n == 11:
##        print("November")
##    elif n == 12:
##        print("December")


# Give the highest number and the position
array = []
for i in range(5):
   array.append(int(input()))
new_array = sorted(array, key = int)
highest_value = new_array[4]

print(highest_value)
print(array.index(highest_value)+1)

