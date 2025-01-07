from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'118.187.59.255/{m}', 0)
    net2 = ip_network(f'118.187.65.115/{m}', 0)
    if net1 != net2:
        print(m)
        break