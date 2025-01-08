from itertools import product

k = 0
al = 'сало'

for i in product(al, repeat=6):
    if 'о' in i:
        if i.count('о') <= 3:
            k += 1

print(k)