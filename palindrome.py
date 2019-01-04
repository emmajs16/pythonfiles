# Emma Stoverink
# November 9, 2018
def reverse(n):
    final_num = 0
    place = 10**(len(str(n))-1)
    for i in range(n):
        x = n % 10
        n = n // 10
        final_num += int(x*place)
        place /=10
    return(final_num)

def is_palindrome(number):
    if reverse(number) == number:
        print("{} is a palindrome!".format(number))
    else:
        print("{} is not a palindrome.".format(number))

is_palindrome(2012)