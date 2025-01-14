

s = open('24/24.txt').readline()

while 'FSRQ' in s: s = s.replace('FSRQ', ' ')

s = s.split(' ')
# print(s, s[0], s[1])

q = 0
for i in range(0, len(s)):

    a = ''.join(s[i:i+81])
    res = len(a) + 4*80+3+3
    q = max(q,res)

print(q)