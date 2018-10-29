# Emma Stoverink
# October 26, 2018

#Prime Factors

user_num = int(input("Please enter an integer: "))
print("The prime factors of {} are:".format(user_num))

for i in range(2, user_num):
    if user_num % i == 0:
        if i % 2 == 0:
            print(i // 2, end = ", ")
            print(2 , end = ", ")
        else:
            print(i, end = ", ")
        user_num = user_num //i