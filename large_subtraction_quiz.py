# Emma Stoverink
# October 3, 2018
import random
import time

print("************************************************************")
print("*{:^58}*".format("Subtraction Quiz"))
print("************************************************************")

num_questions = int(input("\tHow many questions would you like\n\tto answer (5 to 20): "))
print("")
count = 1
correct_answers = 0
# Get the initial time
current_time = time.time()

while count <= num_questions:
    print("\tQuestion {}:".format(count))
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    if num2 > num1:
        num1, num2 = num2, num1
    user_answer = int(input("\t{} - {} = ".format(num1, num2)))
    difference = num1 - num2
    if difference == user_answer:
        print("\t Correct!\n")
        correct_answers +=1
    else:
        print("\tIncorrect...\n")
    count += 1
final_time = time.time
print("************************************************************")
print("Quiz Results:")
print("You answered {} our of {} questions correct!".format(correct_answers,num_questions))
print("Time : {} seconds".format(final_time- current_time))
