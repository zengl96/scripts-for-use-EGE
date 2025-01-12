


from ipaddress import *



net = ip_network('172.16.168.0/255.255.248.0')

print(len([s for s in net]))
c = 0
for ip in net:

    print(bin(int(ip))[2:].count('1'))
    if (bin(int(ip))[2:].count('1'))%5!=0:
        c+=1

print(c)