from ipaddress import *
for m in range(20, -1, -1):
    net = ip_network(f'149.238.225.115/{m}', False)
    k = 0
    for x in net:
        if bin(int(x))[2:].count('1') == 15:
            k += 1
    print(k, m)