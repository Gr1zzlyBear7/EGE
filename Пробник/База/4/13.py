k = 0
from ipaddress import *
net = ip_network('115.192.0.0/255.192.0.0')
for i in net:
    if bin(int(i)).zfill(32).count('1') % 3 != 0:
        k += 1
print(k)