from ipaddress import *

for m in range(32, -1, -1):
    net2 = ip_network(f'157.220.185.237/{m}', False)
    net1 = ip_network(f'157.220.184.230/{m}', False)
    if net1 == net2:
        k = 0
        for i in net1:
           ip = bin(int(i))[2:]
           if ip.count('1') == 15:
               k += 1
        print(k)
        break