from itertools import product

al = 'КАБИНЕТ'
k = 0

for i in product(al, repeat=7):
    if len(set(i)) == len(i):
        if i[-1] not in 'АИЕ':
            k += 1

print(k)