from ipaddress import *

net = ip_network(f'192.168.0.0/255.255.192.0', 0)
k = 0
for i in net:
    if bin(int(i)).count('1') > 16:
        k += 1
print(k)