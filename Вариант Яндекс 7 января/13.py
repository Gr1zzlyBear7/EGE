from ipaddress import ip_network

net = ip_network('192.168.76.160/255.255.255.240', False)
k = 0
z = 1
for i in net.hosts():
    if z % 2 == 0:
        if bin(int(i))[2:].zfill(32)[24:].count('1') % 2 == 0:
            k += 1
    z += 1
print(k)