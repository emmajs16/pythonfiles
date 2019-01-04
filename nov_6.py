
# x = input()
primes = [False] * 101
for i in range(2,len(primes)): # for each element in the array after two, count every num element and change it to True
    for num in range(2, len(primes)):
    if i % 2 == 0:
        primes[i] = True
    if i % 3 == 0:
        primes[i] = True
    if i % 5 == 0:
        primes[i] = True
    if i % 7 == 0:
        primes[i] = True
print(primes)
