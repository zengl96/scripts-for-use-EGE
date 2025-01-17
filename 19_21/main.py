


def f(a, m):

    if a<=17: return m%2==0
    if m == 0: return 0

    h = [f(a-3,m-1), f(a-5, m-1), f(a//2, m-1)]

    return any(h) if m%2!=0 else all(h)

print('19', [s for s in range(18,1000) if f(s,2)])

print('19', [s for s in range(18,1000) if f(s,3) and not f(s,1)])
print('19', [s for s in range(18,1000) if f(s,4) and not f(s,2)])