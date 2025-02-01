from ipaddress import *
k = 0
for m in range(33):
    net = ip_network(f'169.25.132.59/{m}', False)
    if str(net.network_address).count('1') == m:
        for ip in net:
            if bin(int(ip))[2:].count('1') == 11:
                k += 1
print(k)