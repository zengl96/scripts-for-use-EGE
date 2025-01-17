



def f(n,m):

    if n == 24: return 0
    if n == m: return 1

    if n<m: return 0

    return f(n-2,m) + f(n-3,m) + f(n//4,m)

print(f(36,13))
