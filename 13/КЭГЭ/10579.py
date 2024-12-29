from ipaddress import *

k = 0
net = ip_network('192.168.240.0/255.255.255.0')
for i in net:
    if bin(int(i)).count('1') == 16:
        k += 1
print(k)