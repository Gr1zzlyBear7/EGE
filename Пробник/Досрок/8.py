from itertools import product

al = 'ДГИАШЭ'
k = 0
mn = set()
for i in product(al, repeat=5):
    s = ''.join(i)
    if s[0] not in 'ИАЭ':
        if s[-1] not in 'ДГШ':
            k += 1
            print(s)
            mn.add(s)
print(k)
print(len(mn))