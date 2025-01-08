from itertools import product

k = 0
al = 'игрок'

for i in product(al, repeat=5):
    if i[0] != 'к' and 'рок' not in ''.join(i) and i.count('и') == i.count('г') == i.count('р') == i.count('о') == i.count('к') == 1:
        k += 1
        print(i)
print(k)