from itertools import product

al = 'АИМРЯ'
arr = list(product(al, repeat=4))
print(arr.index(tuple('АРИЯ')) + 1)
k = 1
for i in product(al, repeat=4):
    if i == tuple('АРИЯ'):
        print(k)
        break
    k += 1