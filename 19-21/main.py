




def f(a,m):


    if a <= 12: return m%2==0
    if m == 0: return 0

    if a%2 == 0:
        h = [f(a-1,m-1),f(a/2,m-1) ]
    else:
        h = [f(a-1,m-1)]

    return any(h) if m%2!= 0 else all(h)


print('19)', [s for s in range(13,100) if not f(s, 1) and f(s, 2)]) # 25
print('20)', [s for s in range(13,100) if not f(s, 1) and f(s, 3)]) # 50
print('21)', [s for s in range(13,100) if (f(s, 2) or f(s, 4)) and not f(s, 2)]) # 27 51