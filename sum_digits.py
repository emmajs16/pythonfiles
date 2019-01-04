# Emma Stoverink
# November 9, 2018

def sum_digits(n):
    sum = 0
    for i in range(n):
        x = n % 10
        n = n // 10
        sum += x
    print(sum)
    
sum_digits(12345)