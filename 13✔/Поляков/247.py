from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'118.222.130.140/{m}', 0)
    net2 = ip_network(f'118.222.201.140/{m}', 0)
    if net1 == net2:
        print(net1.netmask)
        break