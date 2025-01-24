from itertools import *
al = '01234567'
k = 0
for i in product(al, repeat=6):
    if len(set(i)) == len(i) and i[0] != '0':

        s = ''.join(i)
        s1 = s
        for x in '024':
            s = s.replace(x, '6')
        for x in '135':
            s = s.replace(x, '7')
        if '77' not in s and '66' not in s:
            if int(s1, 8) % 5 == 0:
                k += 1
                print(s1)

print(k)