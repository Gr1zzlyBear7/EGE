from ipaddress import *

for m in range(33):
    net = ip_network(f'111.81.93.127/{m}', 0)
    if '111.81.80.0' in str(net):
        print(net.netmask)