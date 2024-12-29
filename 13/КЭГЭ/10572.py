from ipaddress import *

for i in range(33):
    net = ip_network(f'173.103.25.118/{i}', 0)
    if '173.103.24.0' in str(net):
        print(32 - i)
        break