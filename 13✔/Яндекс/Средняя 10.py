from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240', 0)
k = 0
for i in net:
    if bin(int(i))[2:].zfill(32).count('0') > 21:
        k += 1
print(k)
