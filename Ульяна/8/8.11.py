from itertools import *

al = 'geraclit'
k = 0
for i in product(al, repeat=6):
    if len(set(i)) == len(i):
        s = ''.join(i)
        for x in 'grcl':
            s = s.replace(x, 't')
        for x in 'ea':
            s = s.replace(x, 'i')
        if s.count('t') > s.count('i'):
            if 'ii' not in s:
                k += 1
print(k)