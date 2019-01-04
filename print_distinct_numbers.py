# Emma Stoverink
# November 30, 2018

# Print Distict Numbers

numbers = str(input("Enter numbers (seperated by spaces): "))
numbers = numbers.split()
second_numbers = []
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
i = 0
while i <= (len(numbers)-1):
    current_value = numbers[i]
    if second_numbers.count(current_value) >= 1:
        i += 1
    else:
       second_numbers.append(current_value)
       i += 1
print(second_numbers)
   
    