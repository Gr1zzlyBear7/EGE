k = 0
from ipaddress import *
net = ip_network('87.226.26.72/255.255.255.252')
for i in net:
    if bin(int(i))[2:].zfill(32).count('0') % 2 == 0:
        k += 1
        print(len(bin(int(i))[2:].zfill(32)))
print(k)