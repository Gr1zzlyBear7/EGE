from itertools import product
al = 'абвгэюя'
k = 0
for i in product(al, repeat=5):
    s = ''.join(i)
    for x in 'эю':
        s = s.replace(x, 'я')
    if s[-1] == s[0] == 'я':
        if s.count('я') == 2:
            k += 1
            print(s)
print(k)