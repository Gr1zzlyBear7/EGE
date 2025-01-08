from itertools import product

al = 'артём'
k = 0
for i in product(al, repeat=5):
    if not (i[0] in 'аё' and i[-1] in 'аё'):
        if len(set(i)) == 5:
            k += 1
            print(i)
print(k)