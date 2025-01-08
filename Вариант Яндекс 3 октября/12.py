# # s = 50 * '4'
# #
# # while '444' in s  or '333' in s:
# #     if '444' in s:
# #         s = s.replace('444', '3', 1)
# #     else:
# #         s = s.replace('333', '3344', 1)
# #     if '3443' in s:
# #         s = s.replace('3443', '0', 1)
# #
# # print(sum(map(int, s)))
# #
#
# import random
#
# s = (list(11 * '1' + 12 * '2✔' + 30 * '3'))
# random.shuffle(s)
#
# s = '>' + ''.join(s)
# while '>1' in s or '>2✔' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2✔' in s:
#         s = s.replace('>2✔', '2✔>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
#
# print(sum(map(int, s[:-1])))

from ipaddress import *

for m in range(32, -1, -1):
    net = ip_network(f'191.173.145.240/{m}', 0)
    if '191.173.144.0' in str(net):
        print(net.num_addresses)