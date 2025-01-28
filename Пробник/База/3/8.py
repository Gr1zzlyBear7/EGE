from itertools import product
k = 0
al = '0123456789abcdef'
se = set()
for i in product(al, repeat=5):
    s = ''.join(i)
    if sorted(s) == list(s) and s[0] != '0':
        k += 1
        se.add(s)
        print(s)
print(k, len(se))