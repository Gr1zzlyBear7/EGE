



from itertools import *
al = '0123456789abcdefghij'
k = 0
for i in product(al, repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        if int(s[-1], 20) + int(s[0], 20) == 26:
            for x in '2468acegi':
                s = s.replace(x, '0')
            for x in '3579bdfhj':
                s = s.replace(x, '1')
            if s == '10101' or s == '01010':
                k += 1
print(k)