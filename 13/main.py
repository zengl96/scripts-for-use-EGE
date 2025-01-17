
from ipaddress import *


net = ip_network('123.222.111.192/255.255.255.248', 0)

for i in net:

    a = bin(int(i))[2:].zfill(32)
    print(a)