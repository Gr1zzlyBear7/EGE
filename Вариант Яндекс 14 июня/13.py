from ipaddress import *
net = ip_network('192.168.0.0/255.255.192.0', 0)
k = 0
for i in net:
    ip = bin(int(i))[2:].zfill(32)
    if ip.count('1') > ip.count('0'):
        k += 1
print(k)