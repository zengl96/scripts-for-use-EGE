


from ipaddress import *


for m in range(33):
    net1 = ip_network(f'216.54.187.235/{m}',0)
    net2 = ip_network(f'216.54.174.128/{m}',0)

    if net1.network_address != net2.network_address:

        if net1[0] < IPv4Address('216.54.187.235') < net1[-1]:
            if net2[0] < IPv4Address('216.54.174.128') < net2[-1]:
                print(m)