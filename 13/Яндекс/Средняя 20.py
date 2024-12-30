from ipaddress import *

net = ip_network('192.168.160.0/255.255.224.0', 0)
c = 19
k = 0
for i in net:
    if bin(int(i)).count('1') == c:
        k += 1
print(k)