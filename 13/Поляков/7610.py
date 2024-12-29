from ipaddress import *

net = ip_network('94.253.128.0/255.255.128.0', 0)

k = 0

for i in net:
    ip = bin(int(i))
    if '101' == ip[-3:] and ip.count('1') % 6:
        k += 1

print(k)