from ipaddress import *
for m in range(33):
    net = ip_network(f'118.193.30.139/{m}', False)
    if '118.193.24.0' in str(net):
        print(net.netmask)