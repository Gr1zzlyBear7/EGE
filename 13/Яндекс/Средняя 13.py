from ipaddress import *

net = ip_network('195.102.65.64/255.255.255.192', 0)
k = 0
for ip in net:
    if bin(int(ip))[2:].zfill(0)[25:].count('1') == 4:
        k += 1
print(k)