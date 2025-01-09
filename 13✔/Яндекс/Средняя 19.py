from ipaddress import *

net = ip_network('136.36.240.16✔/255.255.255.248', 0)
k = 0
for i in net:
    if '101' not in bin(int(i))[2:].zfill(32):
        k += 1
print(k)