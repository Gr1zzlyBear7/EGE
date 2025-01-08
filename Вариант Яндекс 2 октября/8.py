from itertools import product

s = 'аекптч'
k = 0
flag = False
z = 0
for i in product(s, repeat=7):
    if 'аптечка' == ''.join(i):
        flag = True
    elif 'печатка' == ''.join(i):
        flag = False
    if flag:
        if z:
            k += 1
        z += 1
print(k)
print(list(product(s, repeat=7)).index(tuple('печатка')) - list(product(s, repeat=7)).index(tuple('аптечка')))