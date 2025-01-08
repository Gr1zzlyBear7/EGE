from itertools import product

k = 0
al = '01234567'

for i in product(al, repeat=5):
    if i[0] != '0' and i.count('1') == 0:
        if len(set(i)) == len(i):
            flag = True
            for x in range(len(i) - 1):
                if i[x] in '0246' and i[x + 1] not in '0246' \
                        or i[x + 1] in '0246' and i[x] not in '0246' \
                        or i[x + 1] in '1357' and i[x] not in '1357' \
                        or i[x] in '1357' and i[x + 1] not in '1357':
                    pass
                else:
                    flag = False
                    break
            if flag:
                k += 1
print(k)
