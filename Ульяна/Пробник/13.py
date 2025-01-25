from ipaddress import *

net = ip_network('204.16.168.0/255.255.248.0', False)
k = 0
for i in net:
    if bin(int(i))[2:].count('1') % 5:
        k += 1
print(k)