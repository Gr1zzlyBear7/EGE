from ipaddress import *
for m in range(33):
    net = ip_network(f'115.12.69.38/{m}', False)
    if '115.12.64.0' in str(net):
        print(m)