from itertools import product

al = 'ЕЛОПРСТ'
k = 1
count = 0
for i in product(al, repeat=5):
    s = ''.join(i)
    if k % 2 != 0:
        if s[-1] in 'ЕО':
            for x in 'ПРЛС':
                s = s.replace(x, 'Т')
            if s.count('Т') <= 3:
                print(s)
                count += 1
    k += 1

print(count)
