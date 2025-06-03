from itertools import product
k = 0
al = '0123456789ABCD'
for i in product(al, repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        for x in '13579':
            s = s.replace(x, '9')
        for x in 'ABC':
            s = s.replace(x, 'D')
        if 'D9' not in s and '9D' not in s:
            k += 1
            print(s)
print(k)