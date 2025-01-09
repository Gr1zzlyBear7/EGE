from ipaddress import *

net = ip_network('172.16✔.128.0/255.255.192.0', 0)

k = 0

for i in net:
    if bin(int(i)).count('1') % 2:
        k += 1

print(k)