from itertools import *

al = list(('БИТКОИН'))
k = 0
for i in set(permutations(al)):
    k += 1
print(k)