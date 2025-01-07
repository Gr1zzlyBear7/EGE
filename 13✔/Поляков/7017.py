from ipaddress import *

for m in range(33):
    net = ip_network(f'229.117.114.172/{m}', 0)
    if '229.117.112.0' in str(net):
        print(m)
        break