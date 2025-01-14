from itertools import  product
from time import sleep


c=0
for i in product('0123456', repeat=7):

    a = ''.join(i)
    if a[0] != '0':
        if a.count('0')+a.count('2')+a.count('4')+a.count('6') == 2:
            c+=1


print(c)