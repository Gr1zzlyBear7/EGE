from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'193.45.192.104/{m}', 0)
    net2 = ip_network(f'193.45.206.210/{m}', 0)
    if net1 == net2:
        k = 0
        for ip in net1:
            if bin(int(ip)).count('1') % 2 == 0:
                k += 1
        print(k)
        break