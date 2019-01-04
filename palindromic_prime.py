# Emma Stoverink
def reverse(n):
    final_num = 0
    place = 10**(len(str(n))-1)
    for i in range(n):
        x = n % 10
        n = n // 10
        final_num += int(x*place)
        place /=10
    return(final_num)

current_palindromic_primes = 0
total_palindromic_primes = 20
num = 3
while True:
    # check to see if it has reached the correct amount of primes
    if current_palindromic_primes == total_palindromic_primes: 
        break
    prime = True
    # check to see if the current number is divisable by anything other than 1 and itself
    for divisor in range(2, num//2+1):
        if num % divisor == 0:
            prime = False
            break
    # if the number is prime print and add one to the current value of primes
    if prime == True:
        # check to see if its also a palindrome
        reversed_num = reverse(num)
        if reversed_num == num:
            print("{:>6}".format(num),end ="")
            current_palindromic_primes += 1
        # if the current number is divisble by 10, start a new line
##        if current_palindromic_primes % 10 == 0:
##            print()
    num = int(num)
    num +=2