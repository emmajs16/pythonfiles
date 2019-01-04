# Emma Stoverink
# November 26, 2018

from random import *

list1 = [2,3,4,1,32]

print("List values:", list1)

print("\nPrint using for loop")
for i in list1:
    print("\t{}".format(i))

print("\nLength of list:", len(list1))
print("Min value of list:", min(list1))
print("Max value of list:", max(list1))
print("Sum of list:", sum(list1))

list1.sort()
print("\nList after sorting:", list1)

shuffle(list1)
print("\nList after shuffling:", list1)