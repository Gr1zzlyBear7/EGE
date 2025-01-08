from itertools import product

k = 0
al = 'гепард'

for i in product(al, repeat=5):
    if i[0] != 'а' and i[-1] !='е' and i.count('г') == 1:
        k += 1

print(k)