from itertools import product

k = 0
al = '123ab'

for i in product(al, repeat=8):
    arr = [1 if x.isalpha() else 0 for x in i]
    if arr.count(1) == 2:
        k += 1

print(k)
