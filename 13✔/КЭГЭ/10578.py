from ipaddress import *

for m in range(33):
    net1 = ip_network(f'10.96.180.231/{m}', 0)
    net2 = ip_network(f'10.96.140.118/{m}', 0)
    if net1 != net2:
        print(32 - m)
        break