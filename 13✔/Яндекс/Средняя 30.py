from ipaddress import *

for m in range(33):
    net1 = ip_network(f'101.96.170.244/{m}', 0)
    net2 = ip_network(f'101.96.126.212/{m}', 0)
    if net2 != net1:
        print(net2.netmask)
        break