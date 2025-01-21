from itertools import product

k = 0
al = 'ГИПЕРБУЛА'
for i in product(al, repeat=6):
    s = ''.join(i)
    for x in 'ИЕУ':
        s = s.replace(x, 'А')
    for x in 'ГПРБ':
        s = s.replace(x, 'Л')
    if s[0] != 'А' and s[-1] != 'А':
        if 'ЛАЛ' not in s:
            k += 1
print(k)