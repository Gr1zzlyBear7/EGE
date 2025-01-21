from ipaddress import *
k = 0
net = ip_network('212.192.32.96/255.255.255.224')
for i in net:
    arr = bin(int(i))[2:].zfill(32)[24:]
    if '111' not in arr and '000' not in arr:
        k += 1
print(k)