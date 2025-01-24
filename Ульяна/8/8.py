from itertools import product

k = 0
al = '0123456789ab'
for i in product(al, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('a') == 2:
            for let in '02468':
                s = s.replace(let, 'a')
            if 'a7' not in s and '7a' not in s:
                k += 1
print(k)