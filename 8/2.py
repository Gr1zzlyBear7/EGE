from itertools import product

k = 0
al = 'abcwxyz'

for i in product(al, repeat=6):
    if i[0] in 'wxyz' and i[-1] in 'wxyz':
        if i.count('w') + i.count('y') + i.count('z') + i.count('x') == 2:
            k += 1

print(k)
