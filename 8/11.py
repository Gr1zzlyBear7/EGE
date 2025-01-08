from itertools import product

k = 0
al = 'вишня'

for i in product(al, repeat=6):
    if i.count('в') <= 1:
        if i[0] != 'ш' and i[-1] not in 'ия':
            k += 1

print(k)