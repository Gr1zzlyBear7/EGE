from ipaddress import *

for i in range(33):
    net = ip_network(f'117.191.138.37/{i}', 0)
    if '117.191.136.0' in str(net):
        print(net.netmask)
        break