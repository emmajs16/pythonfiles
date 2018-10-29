# Emma Stoverink
# October 26, 2018

# Patterns

# Pattern A
for row in range(1, 7):
    for value in range (1, row+1):
        print(value, end = " ")
    print()
    
# Pattern B
print()
for row in range(6, 0, -1):
    for value in range (1, row+1):
        print(value, end = " ")
    print()    
print()

# Pattern C

for row in range(1, 7):
    for i in range(6-row):
        print(" ",end = " ")
    for value in range (row, 0, -1):
        print(value, end = " ")
    print()
print()

# Pattern D
for row in range(6, 0, -1):
    for i in range(6-row):
        print(" ",end = " ")
    for value in range (row, 0, -1):
        print(value, end = " ")
    print()
print()
    