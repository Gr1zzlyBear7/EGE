from ipaddress import *

for m in range(32, -1, -1):
    net = ip_network(f'137.219.220.63/{m}', 0)
    if '255.255.255.255' in str(net):
        print(m)