from itertools import *

al = 'KZBS'
k = 0
for i in product(al, repeat=5):
    s = ''.join(i)
    if s.count('Z') <= 2:
        if 'KB' not in s and 'BK' not in s:
            k += 1
print(k)
