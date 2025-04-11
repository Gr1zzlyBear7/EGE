from itertools import product

# k = 0
# al = '0123456'
# for i in product(al, repeat=6):
#     if i[0] != '0':
#         if i.count('0') == 1:
#             s = ''.join(i)
#             for x in '24':
#                 s = s.replace(x, '6')
#             if s.count('6') % 2 == 0:
#                 k += 1
# print(k)
k = 0
al = ''.join([str(x) for x in range(0, 7)])
for i in product(al, repeat=6):
    if i[0] != '0':
        if i.count('0') == 1:
            s = ''.join(i)
            for x in '24':
                s = s.replace(x, '6')
            if s.count('6') % 2 == 0:
                k += 1
print(k)
