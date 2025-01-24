from itertools import product

al = '0123456789abcd'
k = 0
for i in product(al, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        for x in '1357':
            s = s.replace(x, '9')
        for x in 'abc':
            s = s.replace(x, 'd')
        if '9d' not in s and 'd9' not in s:
            k += 1
print(k)