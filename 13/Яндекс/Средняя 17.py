from ipaddress import *

net = ip_network('114.179.203.128/255.255.255.192')
k = 0
for i in net:
    if bin(int(i)).count('1') % 3 == 0:
        k += 1
print(k)