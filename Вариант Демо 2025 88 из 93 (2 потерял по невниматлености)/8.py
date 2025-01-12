from itertools import product

k = 0
al = '0123456789ab'
for i in product(al, repeat=5):
    if i.count('7') == 1 and i[0] != '0':
        if i.count('9') + i.count('a') + i.count('b') <= 3:
            k += 1

print(k)