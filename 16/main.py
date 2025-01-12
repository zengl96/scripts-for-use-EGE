

from functools import *



@lru_cache(None)
def f(n):

    if n<3:
        return n
    if n%2 != 0 and n>2:
        return f(n-1)+f(n-2)+1
    if n%2 == 0 and n>2:
        sum_ = 0
        for i in range(1,n):
            sum_ += f(i)
        return sum_
    
for i in range(3,4500):
    f(i)

print(f(38))