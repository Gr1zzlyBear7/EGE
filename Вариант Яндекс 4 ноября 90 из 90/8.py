from itertools import product

al = '0123456789abc'
k = 0
evens = '02468ac'
odds = '13579b'
for i in product(al, repeat=7):
    s = ''.join(i)
    if i[0] != '0':
        if i.count('5') >= 2:
            for c in '2468ac':
                s = s.replace(c, '0')
            for c in '3579b':
                s = s.replace(c, '1')
            if '00' not in s and '11' not in s:
                k += 1


print(k)
