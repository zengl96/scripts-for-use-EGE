
from ipaddress import *


net = ip_network('192.168.156.224/255.255.255.240', 0)

for i in net.hosts():

    print(i)