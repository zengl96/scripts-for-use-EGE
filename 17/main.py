




with open('17/17.txt', 'r', encoding='utf-8') as f:

    result = f.read().split('\n')

c = []
for i in range(len(result)-1):

    a,b = result[i], result[i+1]


    if (abs(int(a)) + abs(int(b)))  % 11 == 0:
        c.append(int(a) + int(b))


print(len(c), max(c))