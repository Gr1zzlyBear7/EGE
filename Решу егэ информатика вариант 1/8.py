from itertools import product

al = 'иван'
k = 0
for i in product(al, repeat=5):
    if i.count('и') >= 1:
        k += 1
print(k)