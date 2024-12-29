from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'215.171.155.54/{m}', 0)
    net2 = ip_network(f'215.171.145.37/{m}', 0)
    if net1 == net2:
        print(net1.netmask)
        break
