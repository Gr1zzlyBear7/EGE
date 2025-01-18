from itertools import product

k = 1
ans = []
al = 'БИКНОПР'
for i in product(al, repeat=6):
    if i.count('О') == 3 and len(set(i)) == 4:
        ans.append([k, i])
    k += 1

print(max(ans))