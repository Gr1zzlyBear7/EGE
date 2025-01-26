from itertools import product

al = '01234567'
k = 0
for i in product(al, repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        if len(s) == len(set(s)):
            for x in '024':
                s = s.replace(x, '6')
            for x in '135':
                s = s.replace(x, '7')
            if '66' not in s and '77' not in s:
                k += 1
print(k)