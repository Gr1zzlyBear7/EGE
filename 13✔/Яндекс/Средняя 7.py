from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'121.171.5.70/{m}', 0)
    net2 = ip_network(f'121.171.5.107/{m}', 0)
    if net1 == net2:
        print(net2.num_addresses)
        break