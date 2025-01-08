from itertools import product

al = 'кресло'
k = 0

for i in product(al, repeat=4):
    if i[0] in 'крсл' and i[-1] in 'ео':
        k += 1

print(k)