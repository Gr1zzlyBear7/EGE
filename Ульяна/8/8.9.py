


from itertools import product
k = 0
al = 'VORN'
x = set()
for i in product(al, repeat=5):
    if 'OO' not in ''.join(i):
        k += 1
        x.add(i)
print(len(x), k)