from itertools import product

al = '0123456789ab'
k = 0
for i in product(al, repeat=5):
    if i[0] != '0':
        if i.count('7') == 1:
            if i.count('9') + i.count('a') + i.count('b') <= 3:
                k += 1
                print(i)
print(k)