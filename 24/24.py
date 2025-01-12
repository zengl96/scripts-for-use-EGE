

s = open('24/24_17878.txt').readline()


while '-*' in s: s = s.replace('-*', '- *')
while '*-' in s: s = s.replace('*-', '* -')
while '--' in s: s = s.replace('--', '- -')
while '**' in s: s = s.replace('**', '* *')

s = s.split(' ')
m = 0

for ind in s:

    if len(ind)>m:
        for i in range(len(ind)-1):
            pos = ind[i]
            
            if ind[i] not in '*' and ind[i]+ind[i+1] not in ['00','06', '07','08','09']:

                for j in range(i+1, len(ind)):
                    pos += ind[j]
                    if ind[j] not in '-*':
                        m = max(m, len(pos))


print(m)