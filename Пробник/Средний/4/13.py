from ipaddress import *

net = ip_network('185.8.0.0/255.255.128.0', False)
m = []
for i in net:
    m.append(bin(int(i))[2:].count('1'))
print(max(m))