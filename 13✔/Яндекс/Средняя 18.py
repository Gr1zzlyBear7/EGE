from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240', 0)
k = 0
for i in net:
    if bin(int(i)).count('1') % 2:
        k += 1
print(k)