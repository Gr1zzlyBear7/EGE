from itertools import product

k = 0
al = 'abcd'

for i in product(al, repeat=4):
    if i[0] <= i[1] <= i[2] <= i[3]:
        k += 1

print(k)