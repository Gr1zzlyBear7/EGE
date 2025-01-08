from itertools import *

k = 1
al = 'елмру'

for i in product(al, repeat=4):
    if i[0] == 'л':
        print(k)
        break
    k += 1