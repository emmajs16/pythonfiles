# Emma Stoverink
# October 24, 2018

#Cheap Travel


# n = times she uses the subway
# m = number of times covered by the special ticket
# a = cost of one subway ticket
# b = cost of the special ticket
##n, m, a, b = input().split()
##
##n = int(n) # times she uses the subway
##m = int(m) # number of trips covered by the special ticket
##a = int(a) # cost of one normal ticket
##b = int(b) # cost of one special ticket
##num_special = 0
##num_normal = 0
##
##if n >= m:
##    num_special = n // m
##    num_normal = n % m
##    total_cost_normal = num_normal * a
##    total_cost_special = num_special * b
##    if total_cost_normal > b:
##        num_special +=1
##        num_normal = 0
##else:
##    num_normal = n
##    total_cost_normal = num_normal * a
##    total_cost_special = num_special * b
##
##total_cost_normal = num_normal * a
##total_cost_special = num_special * b
##
##    
##final_sum = total_cost_special + total_cost_normal   
##if final_sum > (n* a):
##    final_sum = n*a
##    
##print(final_sum)


# Multiplication Table

##n, x = input().split()
##n = int(n)
##x = int(x)
##total = 0
##for row in range(1,n+1):
##    for value in range(1,n+1):
##        result = row * value
##        print(result)
##        if result == x:
##            total +=1
##print(total)

# Hulk

##n = int(input())
##if n == 1:
##    print("I hate it")
##else:
##    for i in range(1,n+1):
##        if i % 2 == 1:
##            if i == n:
##                print("I hate it")
##            else:
##                print("I hate that" , end = " ")
##        elif i % 2 == 0:
##            if i == n:
##                print("I love it")
##            else:
##                print("I love that" , end = " ")

# Potatoes

y, k, n = input().split()
y = int(y)
k = int(k)
n = int(n)
possible_x = [5, 10, 3]
##x = 0
##for x in range(0, n):
##    if x+y <= 0 and x + y % k == 0:
##        possible_x.append(x)
##        print(x)
sorted(possible_x, key=int)
print(sorted(possible_x))
