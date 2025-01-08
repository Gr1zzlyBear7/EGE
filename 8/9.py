from itertools import product

k = 0
al = '01234'

for i in product(al, repeat=6):
    if i[0] not in '01' and i[-1] not in '34':
        k += 1

print(k)