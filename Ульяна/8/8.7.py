from itertools import product
al = 'АВИОРТФ'
k = 1
ch = 0
for i in product(al, repeat=7):
    if k % 2:
        s = ''.join(i)
        if s[:4] != 'ТРИО' and s[-4:] != 'ТРИО':
            if 'ТРИО' in s:
                ch += 1
    k += 1
print(ch)