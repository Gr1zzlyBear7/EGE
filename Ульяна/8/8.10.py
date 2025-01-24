from itertools import product
k = 0
al = 'АДЕМИК'
for i in product(al, repeat=8):
    s = ''.join(i)
    if s.count('А') == 2 and s.count('К') == 2 and s.count('Д') == 1 and\
        s.count('Е') == 1 and s.count('М') == 1 and s.count('И') == 1:
        for x in 'АЕ':
            s = s.replace(x, 'И')
        for x in 'КД':
            s = s.replace(x, 'М')
        if 'ММ' not in s and 'ИИ' not in s:
            k += 1
print(k)