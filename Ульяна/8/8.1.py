from itertools import product

k = 0
al = '012345678'
for i in product(al, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('5') == 1:
            if '11' not in s and '22' not in s and '33' not in s and \
                    '44' not in s and '55' not in s and '66' not in s and \
                    '77' not in s and '88' not in s and '00' not in s:
                k += 1
print(k)