# Emma Stoverink
# November 9, 2018

def sum_series(n):
    sum = 0.0
    for i in range(1,n+1):
        x = i + 1
        sum += i/x
        print("{:<3}\t\t{:>8.4f}".format(i,sum))
def main():
    print("{:<3}\t\t{:>8}\n".format("i","m(i)"))
    sum_series(20)
    
main()