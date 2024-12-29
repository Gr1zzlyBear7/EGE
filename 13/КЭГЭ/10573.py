from ipaddress import *

for i in range(32, -1, -1):
    net = ip_network(f'191.173.145.240/{i}', 0)
    if '191.173.144.0' in str(net):
        k = 0
        for ip in net:
            k += 1
        print(k)
        break