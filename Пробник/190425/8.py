from itertools import *

al = 'АБДЕОП'
k = 1
for i in product(al, repeat=6):
    if k % 2 == 0:
        if len(i) == len(set(''.join(i))):
            if i[0] == 'О':
                print(k)

    k += 1