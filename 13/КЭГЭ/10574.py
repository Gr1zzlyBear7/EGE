from ipaddress import *

k = 0
for i in range(33):
    net = ip_network(f'158.116.11.146/{i}', 0)
    if '158.116.0.0' in str(net):
        k += 1
print(k)