from itertools import product

al = 'пуля'

k = 0

for i in product(al, repeat=6):
    if i.count('у') == 2:
        k += 1

print(k)