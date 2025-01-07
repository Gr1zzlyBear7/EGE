from ipaddress import *

net = ip_network('212.192.32.96/255.255.255.224', 0)

k = 0

for i in net:
    new = bin(int(i))[2:].zfill(32)[24:]
    if '111' not in new and '000' not in new:
        k += 1
print(k)