from ipaddress import *

for m in range(32, -1, -1):
    net1 = ip_network(f'61.58.73.42/{m}', 0)
    net2 = ip_network(f'61.58.75.136/{m}', 0)
    if net1 == net2:
        k = 0
        for ip in net1.hosts():
            if bin(int(ip)).count('1') % 2:
                k += 1
        print(k)
        break