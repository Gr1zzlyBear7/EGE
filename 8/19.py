from itertools import *

al = 'агилморт'
k = 1
for i in product(al, repeat=4):
    if ''.join(i[-2:]) == 'им':
        print(i, k)
    k += 1