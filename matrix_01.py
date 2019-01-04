# Emma Stoverink
# November 9, 2018
import random

def print_matrix(n):
    for y in range(n):
        for x in range(n):
            num = random.randint(0,1)
            print(num, end = " ")
        print()
            
def main():
    print_matrix(10)

main()