



for i in range(11071, 10**10, 11071):

    _ = str(i)


    if _[0] in '13579' and _[1:4] == '136' and _[-1] == '1':
            print(i, i/11071)