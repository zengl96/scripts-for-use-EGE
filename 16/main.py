

from functools import *

@lru_cache
def f(n):

    if n<5:
        return 5
    else:
        return 2*n*f(n-4)


for i in range(1,14000):
    f(i)
print((f(13766)-9*f(13762))/f(13758))