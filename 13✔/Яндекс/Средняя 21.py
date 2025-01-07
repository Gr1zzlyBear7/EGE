from ipaddress import *

net1 = ip_network('192.168.56.192/255.255.255.192', 0)
net2 = ip_network('192.168.56.208/255.255.255.240', 0)

n1 = set()
n2 = set()

for i in net1:
    n1.add(bin(int(i))[2:].zfill(32))
for i in net2:
    n2.add(bin(int(i))[2:].zfill(32))
print(len(n1 ^ n2))