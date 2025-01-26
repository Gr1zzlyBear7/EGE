from ipaddress import *

k = 0
net = ip_network('171.128.0.0/255.128.0.0', False)
for i in net.hosts():
    s = bin(int(i))[2:].zfill(32)
    lt = s[:16]
    rt = s[16:]
    if lt.count('1') < rt.count('1'):
        k += 1
print(k)
