from ipaddress import *

k = 0
net = ip_network('192.168.32.160/255.255.255.240')
for i in net:
    if bin(int(i)).count('1') % 2 == 0:
        k += 1
print(k)