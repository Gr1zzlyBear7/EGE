from ipaddress import *

net = ip_network('172.30.0.0/255.254.0.0', 0)

k = 0

for i in net:
    if bin(int(i)).count('1') % 12:
        k += 1
print(k)