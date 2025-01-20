from itertools import product

al = 'АЕКПТЧ'
k = 0
z = 125459
r = 0
for i in product(al, repeat=7):
    if r:
        k += 1
    if ''.join(i) == 'АПТЕЧКА':
        r = 1
    if ''.join(i) == 'ПЕЧАТКА':
        print(k - 1) # вычитаем саму печатку
        break
arr = list(product(al, repeat=7))
print(len(arr[arr.index(tuple('АПТЕЧКА')) + 1:arr.index(tuple('ПЕЧАТКА'))]))