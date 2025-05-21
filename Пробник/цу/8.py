from itertools import *

k = 0
al = '012345678'
for i in product(al, repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        if i.count('3') == 1:
            for x in '567':
                s = s.replace(x, '8')
            if '38' not in s and '83' not in s:
                k += 1

print(k)