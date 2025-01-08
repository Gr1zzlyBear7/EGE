from itertools import product

k = 0
al = 'дейкстра'
for i in product(al, repeat=6):
    if i.count('й') == 1:
        if len(set(i)) == len(i):
            if i.index('й') != 5:
                if i[i.index('й') + 1] in 'дкстр':
                    k += 1

print(k)
