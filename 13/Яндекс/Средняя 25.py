from ipaddress import *

for m in range(33):
    net = ip_network(f'111.81.27.208/{m}', 0)
    if '111.81.27.192' in str(net):
        print(net.netmask)
        break