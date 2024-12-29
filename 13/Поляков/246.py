from ipaddress import *

for m in range(33):
    net = ip_network(f'124.128.112.142/{m}', 0)
    if '124.128.64.0' in str(net):
        print(net.netmask)
        break