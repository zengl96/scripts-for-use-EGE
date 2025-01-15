

from functools import lru_cache


@lru_cache(None)
def f(n):

    if n == 0:
        return 0
    if n<3:
        return 1
    if n>=3:
        return f(n-1)+f(n-2)

for i in range(1,48):
    print(f(i))
print(f(47))