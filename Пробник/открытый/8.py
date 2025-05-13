from itertools import *

al = ''.join([str(x) for x in range(0, 10)])
k = 0
print(al)
for i in product(al, repeat=4):
    s = ''.join(i)
    if len(set(s)) == 4 and s[0] != '0':
        for x in '0246':
            s = s.replace(x, '8')
        for x in '1357':
            s = s.replace(x, '9')
        if '88' not in s and '99' not in s:
            k += 1
print(k)
