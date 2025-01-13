


for n in range(2, 1000):

    s = '59' + '8'*n

    while '68' in s or '988' in s or '888' in s:


        if '68' in s:
            s = s.replace('68', '8',1)
        if '988' in s:
            s = s.replace('988', '86',1)
        if '888' in s:
            s = s.replace('888', '9',1)


    sum_ = 0
    for i in s:
        sum_ += int(i)
    print(sum_, n)
    if str(sum_ ** (1/3)).split('.')[-1] == '0':

        break