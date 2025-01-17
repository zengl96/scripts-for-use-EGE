

def f(n):

    _ = set()


    for i in range(1,int(n**0.5)+1):

        if n%i==0:
            _.add(i), _.add(n//i)

    return sum(_)

for i in range(1000, 9999+1):
    
    if str(f(i))[-2:] == '23':
        print(i, f(i))