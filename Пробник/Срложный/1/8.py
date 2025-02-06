from itertools import product
al = list('ПАВСКИЙ')
al.sort()
al = ''.join(al)
k = 1
for i in product(al, repeat=6):
    s = ''.join(i)
    s = s.replace('А', 'И')
    if 'ИИ' in s:
        if s == 'КИКИИИ':
            print(k)
            break
        k += 1