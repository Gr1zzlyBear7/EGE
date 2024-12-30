from ipaddress import *

net = ip_network('192.168.76.160/255.255.255.240', 0)
num = 1
k = 0
for ip in net:
    rt = bin(int(ip))[2:].zfill(32)[24:]
    if num % 2 == 0 and rt.count('1') % 2 == 0:
        k += 1
        print(bin(int(ip))[2:].zfill(32))
    num += 1
print(k - 1)