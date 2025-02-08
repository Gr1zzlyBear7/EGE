# from itertools import product
# al = '0123456789'
# for i in range(ord('a'), ord('a') + 32):
#     al += (chr(i))
# print(len(al))
# odds = ''.join([al[x] for x in range(1, len(al), 2)])[1:]
# print(odds)
# k = 0
# for i in product(al, repeat=6):
#     if i[0] != '0':
#         if i.count('6') == 1:
#             s = ''.join(i)
#             for x in odds:
#                 s = s.replace(x, '1')
#             if '61' not in s and '16' not in s:
#                 k += 1
# print(k)
# не подсчитает, только руками, т.к. 42 ** 6 больше 5 лярдов

k = 0
k += 1 * 20 * 41 * 41 * 41 * 41
k += 19 * 1 * 20 * 41 * 41 * 41
k += 40 * 20 * 1 * 20 * 41 * 41
k += 40 * 41 * 20 * 1 * 20 * 41
k += 40 * 41 * 41 * 20 * 1 * 20
k += 40 * 41 * 41 * 41 * 20 * 1
print(k)