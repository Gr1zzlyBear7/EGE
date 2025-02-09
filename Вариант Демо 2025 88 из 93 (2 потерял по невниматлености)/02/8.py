from itertools import product
al = '0123456789ab'
k = 0
for i in product(al, repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        if s.count('7') == 1:
            if s.count('9') + s.count('a') + s.count('b') <= 3:
                k += 1
print(k)