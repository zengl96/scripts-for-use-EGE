
from math import *


def nod(n,m,k):

    del_n = set()
    del_m = set()
    for i in range(1,int(n**0.5)+1):

        if n%i==0:
            del_n.add(i), del_n.add(n//i)

    for i in range(1,int(m**0.5)+1):

        if m%i==0:
            del_m.add(i), del_m.add(m//i)

    max_dell = max(del_n.intersection(del_m))


    return 1 if max_dell == k else 0

_ = True
c = 0
# u = set()
# for A in range(1,1001):

#     for x in range(1,1500):
#         if (  gcd(A,420)==2 or ( (not gcd(A,x))==12 <= (not gcd(110,x))==1 )    ) == 0:
#             _ = False
#             u.add(A)
#             break

#     if _ == True:
#         c+=1

#     _ = True


y =set()
for A in range(1,1001):

    for x in range(1,1500):
        if (  nod(A,420,2) or ( (not nod(A,x,12)) <= (not nod(110,x,11)) )    ) == 0:
            _ = False
            y.add(A)
            break

    if _ == True:
        c+=1

    _ = True

print(c)

print(gcd(646,420), nod(646,420, 2))
# print(y.difference(u))