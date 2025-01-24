from itertools import product
k = 0
al = '01234567'
for i in product(al, repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        arr = [x for x in s if x in '0246']
        if len(arr) == 2:
            for x in '13':
                s = s.replace(x, '5')
            if '75' not in s and '57' not in s and '77' not in s:
                k += 1
print(k)
