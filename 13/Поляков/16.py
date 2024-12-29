from ipaddress import *

for m in range(33):
    net = ip_network(f'111.81.208.27/{m}', False)
    if '111.81.192.0' in str(net):
        print(net.netmask)
        break