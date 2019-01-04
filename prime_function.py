# Emma Stoveink
# November 9, 2018

def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return(prime)
def main():
    user_number = int(input("Enter an integer: "))
    if is_prime(user_number):
        print("{} is a prime number.".format(user_number))
    else:
        print("{} is not a prime number.".format(user_number))
main()