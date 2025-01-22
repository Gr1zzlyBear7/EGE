from ipaddress import *

k = 0
for m in range(32, -1, -1):
    net = ip_network(f'61.58.73.42/{m}', False)
    net_2 = ip_network(f'61.58.75.136/{m}', False)
    if net == net_2:
        k = 0
        for x in net.hosts():
            if bin(int(x)).count('1') % 2:
                k += 1
        print(m, k)