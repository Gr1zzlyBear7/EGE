from ipaddress import *

for i in range(33):
    net = ip_network(f'122.21.49.91/{i}', 0)
    if '122.21.48.0' in str(net):
        print(i)
        break