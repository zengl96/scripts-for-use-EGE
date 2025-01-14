




def f(n):


    b = bin(n)[2:]

    if b.count('1')%2==0:
        b  = b+'0'
        b = '11'+b[2:]

    else:

        b = b+'1'
        b = '10' + b[2:]

    return int(b, 2)


print(max(f(n) for n in range(1000) if n<50))