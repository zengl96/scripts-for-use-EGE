


from ipaddress import *


for A in range(1,256):
    net1 = ip_network(f'116.242.{A}.26/255.255.255.224',0)
    _ = True
    for i in net1:
        i = bin(int(i))[2:].zfill(32)
        if i[:16].count('1') < i[16:].count('1'):
            _ = False

    if _ == True:
        print(A)

    _ = True