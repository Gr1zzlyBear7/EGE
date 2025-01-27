from ipaddress import *

for m in range(33):
    net1 = ip_network(f'193.175.175.231/{m}', False)
    net2 = ip_network(f'193.175.176.118/{m}', False)
    if net1 != net2:
        print(net2.netmask)
        break