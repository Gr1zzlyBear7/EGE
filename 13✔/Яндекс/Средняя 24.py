from ipaddress import *

for i in range(32, -1, -1):
    net = ip_network(f'117.73.208.27/{i}', 0)
    if '117.73.192.0' in str(net):
        print(32 - i)
        break