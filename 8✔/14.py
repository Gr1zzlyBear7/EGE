from itertools import product

k = 0
al = '0123456789'

for i in product(al, repeat=3):
    if i[0] != '0':
        if i[0] <= i[1] <= i[2]:
            k += 1

print(k)