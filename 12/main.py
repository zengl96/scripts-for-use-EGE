



k = '3'*111

while '33333' in k or '1111' in k or '1122' in k:

    
    if '33333' in k:
        k = k.replace('33333','111',1)
    if '1111' in k:
        k = k.replace('111','33',1)

print(k)