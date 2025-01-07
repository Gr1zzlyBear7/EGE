from ipaddress import *

for m in range(33):
    net1 = ip_network(f'161.137.200.35/{m}', 0)
    net2 = ip_network(f'161.137.150.118/{m}', 0)
    if net1 != net2:
        print(net1.netmask)
        break