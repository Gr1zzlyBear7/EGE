from ipaddress import *

net = ip_network('10.112.0.0/255.248.0.0', 0)

k = 0
for i in net:
    if bin(int(i)).count('1') % 3 == 0:
        k += 1
print(k)