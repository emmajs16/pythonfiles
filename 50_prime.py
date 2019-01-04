# Emma Stoverink
# October 31, 2018
# First 50 prime numbers

total_primes = int(input("How many prime numbers do you want? "))
current_primes = 1
num = 3
print("These are the first {} prime numbers:".format(total_primes),end = "\n\n")
print("{:>6}".format(2),end ="")
while True:
    # check to see if it has reached the correct amount of primes
    if current_primes == total_primes: 
        break
    prime = True
    # check to see if the current number is divisable by anything other than 1 and itself
    for divisor in range(2, num//2+1):
        if num % divisor == 0:
            prime = False
            break
    # if the number is prime print and add one to the current value of primes
    if prime == True:
        print("{:>6}".format(num),end ="")
        current_primes += 1
        # if the current number is divisble by 10, start a new line
        if current_primes % 10 == 0:
            print()
    num +=2
