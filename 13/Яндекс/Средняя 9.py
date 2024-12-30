from ipaddress import *

for a in range(255, -1, -1):
    net = ip_network(f'248.112.{a}.35/255.255.255.240', 0)
    flag = True
    for ip in net:
        new_ip = bin(int(ip)).zfill(32)[2:]
        if new_ip[:17].count('0') <= new_ip[17:].count('0'):
            pass
        else:
            flag = False
    if flag:
        print(a)
        break