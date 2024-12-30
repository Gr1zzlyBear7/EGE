from ipaddress import *

k = 0
net = ip_network('95.112.224.0/255.255.255.128', 0)

for i in net:
    ip = bin(int(i))[2:].zfill(32)
    last = ip[24:]
    if last == last[::-1]:
        k += 1
print(k)