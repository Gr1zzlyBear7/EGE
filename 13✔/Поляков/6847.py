from ipaddress import *

net = ip_network('202.75.38.152/255.255.255.248', 0)

k = 0

for i in net:
    if '111' in bin(int(i)):
        k += 1

print(k)