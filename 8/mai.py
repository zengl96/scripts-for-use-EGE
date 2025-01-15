from itertools import  permutations
from time import sleep


c=[]
for i in permutations('марина'):

    a = ''.join(i)
    if a[0] not in 'аи' and a not in c:
        c.append(a)


print(len(c))