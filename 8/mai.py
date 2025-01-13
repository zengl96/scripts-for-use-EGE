from itertools import  product
from time import sleep
k = 0


def _(n):
    return n%2 == 0

for i in product([i for i in range(20)],repeat = 5):

    if (any(list(map(_, i[::2]))) == False and all(list(map(_, i[1::2]))) == True) or (all(list(map(_, i[::2]))) == True and any(list(map(_, i[1::2]))) == False):

        if (i[0] + i[-1]) == 26:

            k +=1

print(k)