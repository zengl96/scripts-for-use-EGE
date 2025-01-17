

s = open('24/24.txt').readline()

s = s.replace('X', ' ')

s = s.split(' ')

s = sorted(s, key=lambda x: x.count('Y'), reverse=1)

for i in s:
    print(i, len(i), i.count('Y'))
    input()