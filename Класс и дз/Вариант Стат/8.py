from itertools import product
print(int('50000000', 15) < 855_000_000)
al = '0123456789abcde'
k = 0
for i in product(al, repeat=8):
    if i[0] != '0':
        if i[0] < '5':
            if len(set(i)) == len(i):
                k += 1
print(k)