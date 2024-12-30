from ipaddress import *

for m in range(32, -1, -1):
    net = ip_network(f'242.190.196.159/{m}', 0)
    if str(net.broadcast_address) != '242.190.196.159':
        print(m)
        break