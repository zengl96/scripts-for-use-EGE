




with open('17/17.txt', 'r', encoding='utf-8') as f:

    result = f.read().split('\n')


res = list(map(int, result))

minn = 7854390625

qw = []
for i in range(len(res)-2):
    k = 0
    a,b,c = res[i:i+3]

    if 1000 <= abs(a) <= 9999:
        k +=1
    if 1000 <= abs(b) <= 9999:
        k +=1
    if 1000 <= abs(c) <= 9999:
        k +=1

    if k >= 2:
        if a*b*c <= minn:
            _ = a*b*c
            _ = str(_)
            qw.append(_)

print(max(list(map(int, qw))), len(qw))