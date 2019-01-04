# Emma Stoverink
# November 30, 2018
# Analyze scores

scores = str(input("Enter scores (seperated by spaces): "))
scores = scores.split()
sum = 0
above = 0
below = 0
for i in range(0,len(scores)):
    scores[i] = int(scores[i])
    sum += scores[i]

average = sum / len(scores)   

for i in range(0, len(scores)):
    if scores[i] >= average:
        above += 1
    else:
        below += 1
print("There are {} numbers above or equal to the average.".format(above))
print("There are {} numbers below the average.".format(below))