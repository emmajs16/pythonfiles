# Emma Stoverink
# October 29, 2018
# Full triangle

lines = int(input("Enter the number of lines:"))

for row in range(1, lines+1):
    for i in range(6-row):
        print(" ",end = " ")
    for value in range (row, 0, -1):
        print(value, end = " ")
    for value in range (2, row+1):
        print(value, end = " ")
    print()
print()


