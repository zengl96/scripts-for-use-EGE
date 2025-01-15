

s = open('24/24.txt').readline()


while 'Z' in s: s = s.replace('Z', ' ')

s = s.split(' ')

n = []

for i in s:
    k = 1
    try:
        first = i[0]
        for j in i[1:]:
            if j != first:
                k +=1
                first = j
            elif j == first:
                n.append(k)
                break

    except: pass
    finally: n.append(k)

print(max(n))