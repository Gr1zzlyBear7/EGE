from itertools import *

k = 1
al = 'аимря'

for i in product(al, repeat=4):
    if k == 211:
        print(''.join(i))
        break
    k += 1