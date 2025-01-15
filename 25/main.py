

for i in range(0,10**10,1996):

    i = str(i)

    if i[:4] == '1592' and i[-1] == '8' and i[-3]=='6':
        if ('1' not in i[4:-3] and '3' not in i[4:-3] and '5' not in i[4:-3] and '7' not in i[4:-3] and '9' not in i[4:-3]) or i[4:-3] == '':
            print(i, int(i)//1996)