from itertools import product

k = 0
al = 'абиколун'
newnew = [''.join(x) for x in list(product('аиоу', repeat=2)) if x != x[::-1]]
new = [''.join(x) for x in list(product('бклн', repeat=2)) if x != x[::-1]]
for i in product(al, repeat=8):
    if i.count('а') == i.count('б') == i.count('и') == i.count('к') == i.count('о') == i.count('л') == i.count(
            'у') == i.count('н'):
        flag = True
        for x in range(len(i) - 1):
            if i[x] + i[x + 1] in new or i[x] + i[x + 1] in newnew:
                flag = False
                break
        if flag:
            k += 1

print(k)
