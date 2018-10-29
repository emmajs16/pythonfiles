# Emma Stoverink
# October 24, 2018

# Build a pyramid out of stars

num_stars = int(input("Please enter a number of stars: "))

for i in range(1, num_stars+1):
    for j in range(1, i+1):
        print("*",end = "")
    print()

for i in range(num_stars, 0, -1):
    for j in range(i+1, 1 ,-1):
        print("*",end = "")
    print()
