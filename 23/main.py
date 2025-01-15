



def f(n, m, k=5):

    if k >= 0:
        if n==m: return 0
        elif k == 0: return 1
    # if n == 20:
    #     return 0
    # if n == m: return 1
    # if n>m: return 0

    return f(n+1,m, k-1) and f(n*2,m,k-1)

# print(f(1,2,5))
for m in range(1,20):

    print(f(1,m, 5), m)