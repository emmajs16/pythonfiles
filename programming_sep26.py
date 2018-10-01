
def array_replacement():
    X=[]
    for i in range(10):
        X.append(int(input()))

    for i in range(10):
        if X[i]<= 0:
            x = 1
            print("X[{}] = {}".format(i,x))
        else:
            x = X[i]
            print("X[{}] =".format(i), x)

def array_fill():
    N=[]
    V = int(input())
    X = V
    N.append(X)
    for i in range(10):
        X *=2
        N.append(X)
        print("N[{}] =".format(i),N[i])

def array_change():
    N=[]
    for i in range(20):
        N.append(int(input()))
    for i in range(20):
        if i < 10:
            N[i], N[(19-i)] = N[(19-i)], N[i]
        Y= N[i]
        print("X[{}] =".format(i),Y)

def banana():
    # k = cost of first banana
    # n = money he has
    # w = number of bananas
    k, n, w = int(input()), int(input()), int(input())
    i = 1
    total_cost = 0
    while i <= w:
        total_cost += k*i
        i += 1
    final = abs(n-total_cost)
    if final <= 0:
        final = 0
    print(final)
banana()
