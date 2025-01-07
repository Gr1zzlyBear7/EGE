from ipaddress import *

for m in range(31, -1, -1):
    net = ip_network(f'137.219.220.63/{m}', 0)
    if str(net.broadcast_address) in str(net):
        print(m)
        # неправильно