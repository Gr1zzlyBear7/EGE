from itertools import product

k = 0
al = 'вайфу'

for i in product(al, repeat=4):
    if len(set(i)) == len(i):
        if i[0] != 'й':
            if 'вф' not in ''.join(i) and 'фв' not in ''.join(i):
                k += 1

print(k)