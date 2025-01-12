
from itertools import product




a = product('123', repeat=5)

c = 0
for i in a:

    _ = ''.join(i)
    if _[0] == '1':
        c +=1

print(c)