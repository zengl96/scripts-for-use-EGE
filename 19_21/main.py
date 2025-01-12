


def f(n, m):

    if n >= 313: return m%2==0
    if m == 0: return 0

    h = [f(n+2,m-1), f(n+3,m-1), f(n*3,m-1)]

    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(103, 104) if f(s,2)]) 