from ipaddress import ip_network

for m in range(33):
    net = ip_network(f'20.24.110.42/{m}', False)
    if '20.24.96.0' in str(net):
        print(m)