


def dell(n,m):
    return n%m==0

def f(x,A):

    return dell(x,A)or((70<=x<=90)<=(not dell(x,22)))

_ = True
for A in range(1, 1000):
    for x in range(1,1500):

        if f(x,A) == 0:
            _ = False

    if _ == True:
        print(A)
    _ = True