from itertools import product
al = 'АВНРЬЯ'
k = 1
arr = list(product(al, repeat=5))
print(arr.index(tuple('ЬЯРЯР')) + 1)
for i in product(al, repeat=5):
    s = ''.join(i)
    if s[0] != 'Я':
        if s.count('Ь') <= 1:
            if 'ЯЯ' not in s:
                print(s, k)
    k += 1