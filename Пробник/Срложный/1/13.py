from ipaddress import *
for m in range(33):
    net = ip_network(f'204.108.112.142/{m}', False)
    if '204.108.64.0' in str(net):
        print(32 - m)