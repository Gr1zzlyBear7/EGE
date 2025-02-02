from itertools import product
al = 'екмопртью'
k = 1
for i in product(al, repeat=5):
    if i[0] != 'ь' and i.count('к') == 2 and k % 2 == 1:
        print(k, i)
    k += 1