from itertools import  product
from time import sleep


k = 0
for i in product('люстра', repeat=5):

    a = ''.join(i)

    if a.count('ю') <3 and a[-1] not in 'лстр':
        print(a)
        k+=1

print(k)   