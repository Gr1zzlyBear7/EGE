from ipaddress import *

for m in range(33):
    net1 = ip_network(f'10.227.3.113/{m}', 0)
    net2 = ip_network(f'10.235.127.7/{m}', 0)
    if net1 != net2:
        print(m)
        break