




def f(n):

    b = bin(n)[2:]

    if n%5==0: 
        b = b[:3]+b
    else:
        b = b+bin(((n%5)*5))[2:]

    return int(b,2)


print(max([n for n in range(1,1000,2) if f(n)<313]))