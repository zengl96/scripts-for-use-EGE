
def s(n, q):
    _ = ''
    while n != 0:
        _ += str(n%3)
        n = n//3

    return _[::-1]

def f(N):

    b = s(N, 3)

    if N%3 == 0:
        b = '1' + b + '02'
    else:
        b = b  + s(N%3*4, 3)

    return int(b, 3)


print(max([N for N in range(1,10000) if f(N) < 199]))