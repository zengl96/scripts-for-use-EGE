


from itertools import product




f = product('пуля', repeat=6)

c = 0
for a in f:

    _ = ''.join(a)
    if _.count('у') == 2:
        c +=1

print(c)