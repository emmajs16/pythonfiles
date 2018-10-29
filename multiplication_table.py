# Emma Stoverink
# October 8, 2018

# PRINT HEADER
print("\t     Multiplication Table\n")
print("   ", end ="")
for i in range(1,13):
    print("{:4d}".format(i), end = "")
print("\n----------------------------------------------------")

# PRINT BODY
for row in range(1,13):
    print("{:<2}|".format(row),end = "")
    for value in range(1,13):
        result = row * value
        print("{:4d}".format(result), end = "")
    print("\n")