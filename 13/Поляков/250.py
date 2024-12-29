from ipaddress import *

for m in range(32, -1, -1):
    net = ip_network(f'111.81.200.27/{m}', 0)
    if '111.81.192.0' in str(net):
        print(net.netmask)
        break