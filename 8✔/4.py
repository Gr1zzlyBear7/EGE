from itertools import product

al = 'лодка'

k = 0

for i in product(al, repeat=4):
    if i.count('о') >= 2:
        k += 1

print(k)