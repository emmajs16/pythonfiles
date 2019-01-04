# Emma Stoverink
# November 9, 2018

def reverse(n):
    final_num = 0
    place = 10**(len(str(n))-1)
    for i in range(n):
        x = n % 10
        n = n // 10
        final_num += x*place
        place /=10
    print(int(final_num))
reverse(5432)