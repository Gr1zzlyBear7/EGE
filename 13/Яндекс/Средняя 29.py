from ipaddress import *

net = ip_network('123.222.0.192/255.255.255.224', 0)
k = 0
for i in net:
    if bin(int(i)).count('1') == 16:
        k += 1
print(k)