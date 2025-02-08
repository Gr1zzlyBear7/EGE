from ipaddress import *
for m in range(33):
    net = ip_network(f'251.211.38.240/{m}', False)
    if '251.211.38.0' in str(net):
        print(m)