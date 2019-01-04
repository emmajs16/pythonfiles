# Emma Stoverink
# November 30,2018

# Reverse list
numbers = []
reverse_numbers = []
print("Enter 5 numbers (one per line): ")
for i in range(5):
    numbers.append(int(input()))
    
for x in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[x])
    
for num in range(0,len(reverse_numbers)):
    print(reverse_numbers[num])