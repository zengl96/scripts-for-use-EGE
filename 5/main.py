




def f(n):


    b = bin(n)[2:]

    if n%2 == 0:
        b = b+b[-2:]
    else:
        b = '1'+b+'1'

    return int(b, 2)

print(min([f(s) for s in range(1,1000) if f(s)>130]))