



for x in '0123456789abcdefghijklmnopqrstuvxy'.upper():

    a = int(f'6{x}QR{x}',35) + int(f'{x}59SH',35) + int(f'PH{x}69YW',35)
    
    most_popular = {}
    for i in str(a):

        most_popular[int(i)] = str(a).count(i)

    most_popular = sorted(most_popular, key=lambda x: most_popular[x], reverse=True)[0]
    

    if a % most_popular**2 == 0:
        print(a)
