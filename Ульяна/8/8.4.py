from itertools import product

k = 0
al = '012345'
for i in product(al, repeat=6):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('2') == 1:
            for x in '13':
                s = s.replace(x, '5')
            if '52' not in s and '25' not in s:
                k += 1
print(k)