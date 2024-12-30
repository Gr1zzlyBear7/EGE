from ipaddress import *

for A in range(256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    flag = True
    for ip in net:
        new = bin(int(ip))[2:].zfill(32)
        if new[17:].count('1') > 3:
            pass
        else:
            flag = False
    if flag:
        print(A)
        break