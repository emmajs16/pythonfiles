# Emma Stoverink
# November 28, 2018
counts = 10*[0]
while True:
    num = int(input("Please enter a non-negative number (or a negative to stop): "))
    if num <=0:
        break
    elif num > 9:
        print("Please keepy numbers less than 10")
    else:
        counts[num]+=1
for i in range(len(counts)):
    print("Number of {}'s entered: {}".format(i,counts[i])) 

     
