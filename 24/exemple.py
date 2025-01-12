

s = open('24/24_18029.txt').readline()


while 'X' in s: s = s.replace('X', ' '+'1'+' ')

m = 0
j = 0
s = s.split(' ')
for i in range(len(s)-1):
    a = s[i]+s[i+1]
    if len(a)> m:
        m = max(m, a.count('Y'))
        j = len(a)+1
print(m, j)