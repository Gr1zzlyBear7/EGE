from itertools import product
k = 0
al = list('МЫСЛЬ')
al.sort()
al = ''.join(al)
arr = list(product(al, repeat=5))
print(arr.index(tuple('ЫЫЬЬЫ')) + 1)
for i in product(al, repeat=5):
    s = ''.join(i)
    k += 1
    if s[:2] == 'ЫЫ':
        print(s, k)

