from itertools import product

al = 'АЙЛМ'
k = 1
for i in product(al, repeat=5):
    if i.count('М') == i.count('Л') == 0:
        if 'ЙЙ' not in ''.join(i):
            print(i, k)
    k += 1