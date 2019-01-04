def lucky_ticket():
    lucky_ticket = True
    sum_first_half = 0
    sum_second_half = 0
    # input length of ticket
    ticket_length = int(input())
    # ticket number
    ticket_num = str(input())
    # check to see if the ticket number only contains 4 and 7
    for i in range(0, ticket_length):
        if ticket_num[i] != "4" and ticket_num[i] != "7":
            lucky_ticket = False

    # check to see if the sum of the first half of the ticket num is equal to sum of the second half
    for i in range(0,ticket_length//2):
        value = int(ticket_num[i])
        sum_first_half += value
    for i in range(ticket_length-1,ticket_length//2-1,-1):
        value = int(ticket_num[i])
        sum_second_half += value

    if sum_first_half != sum_second_half:
        lucky_ticket = False
    # display if it is a lucky ticket or not
    if lucky_ticket == True:
        print("YES")
    else:
        print("NO")


##lucky_ticket()


def automatic_answer():
    all_nums = []
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        result = ((n * 567)/9)+7492
        result = ((result * 235)/47)- 498
        all_nums.append(int(result))

    for num in range(num_test_cases):
        current = str(all_nums[num])
        tens = current[len(current)-2]
        print(tens)
##automatic_answer()





def complicated_gcd():
    num1, num2 = input().split()
    print(num1,num2)
    # num1 = int(num1)
    # num2 = int(num2)
    # if num2 > num1:
    #     num1,num2 = num2,num1
    # for i in range(num2,num2/2,-1):
    #     if num1 % i == 0 and num2 % i == 0:
    #         gcd = i
    #         break
complicated_gcd()
