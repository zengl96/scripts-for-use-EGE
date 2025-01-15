


for n in range(4, 1000):

    k = '5'+'2'*n

    while '52' in k or '2222' in k or '1122' in k:

        if '52' in k:
            k = k.replace('52','11',1)
        if '2222' in k:
            k = k.replace('2222','5',1)
        if '1122' in k:
            k = k.replace('1122','25',1)

    if sum(list(map(int,k))) == 64:
        print(n)
            
            
